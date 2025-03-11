import concurrent
import concurrent.futures
import html2text
import json
import logging
import openai
import re
import requests
import time
import warnings

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

from typing import Optional, Tuple, Union, List
from contextlib import contextmanager

html2text_markdown_converter = html2text.HTML2Text()
html2text_markdown_converter.wrap_links = False
html2text_markdown_converter.ignore_links = False
html2text_markdown_converter.body_width = 0  # Disable line wrapping

SYSTEMPROMPT = "I have scraped a webpage, and converted it from HTML into Markdown format. I'd like you to answer some questions about it."
INVPROMPT_NOT_EVERY_LINE_RELEVANT = """
No, not every line is relevant to the page's purpose or topic, and a human user would find many lines unhelpful. The page contains various elements, including:

1. **Navigation Links**: Lines that provide links to other sections of the website. These are not directly related to the specific content of the page.

2. **Images and Icons**: Lines that include images, such as social media icons. While they contribute to the overall design and branding of the page, they do not pertain to its specific topic.

3. **Footnotes and References**: Lines that contain footnotes and references. While they provide context and support for the information presented, they may not be essential for understanding the main content.

4. **Feedback and Contact Information**: Lines that invite user feedback or provide contact information. These are useful for user interaction but are not directly related to the content.

5. **Copyright, Cookie Policy Notices, FOIA Notices, etc.**: Lines that provide standard legal notifications for users. They are typically "boilerplate", and do not relate to the page's content.

6. **Login and User Management**: Lines that allow a user to sign into the website. This can provide a personalized user experience, but is not directly relevant to the page's content.

7. **Page Version History**: Lines that discuss the page's version history generally aren't relevant to the page's content.

8. **Advertisement**: Lines that contain advertisements aren't relevant to the page's content.

And so on.

Overall, while many lines contribute to the page's functionality and user experience, not all are directly relevant to the page's specific topic.
A human user who has come to this page for purposes of reading and research would ignore many of these lines.
"""


LOGGER = logging.getLogger("webpage2content")
_LOGGING_CONSOLE_HANDLER = logging.StreamHandler()
_LOGGING_FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
_LOGGING_CONSOLE_HANDLER.setFormatter(_LOGGING_FORMATTER)
LOGGER.addHandler(_LOGGING_CONSOLE_HANDLER)


# With the help of this function, we can prevent urllib3 from spewing obnoxious
# warnings about SSL certificates and other HTTP-related stuff while fetching URLs.
@contextmanager
def suppress_warnings():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        yield


def create_selenium_driver(
    chrome_binary_location: str,
    chromedriver_binary_location: str,
) -> webdriver:
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument(
        "--disable-dev-shm-usage"
    )  # Overcome limited resource problems

    chrome_options.add_argument("--disk-cache-size=0")  # Don't fill up /tmp

    chrome_options.binary_location = chrome_binary_location

    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    )
    chrome_options.add_argument(
        "accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    )

    service = Service(chromedriver_binary_location)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


# Fix a ridiculous formatting error in which sometimes links get double slashes.
def _remove_double_slashes(url: str):
    m = re.match(r"^(\w+)\:(/*)(.*)", url)
    if not m:
        # Doesn't start with a protocol designator. Doesn't look like a URL.
        return url

    protocol = m.group(1)

    s = m.group(3)
    s = re.sub(r"/+", "/", s)

    retval = f"{protocol}://{s}"
    return retval


def _get_html_content_via_requests(url: str) -> str:
    LOGGER.debug(f"Fetching URL {url} with requests")

    response = None

    NUM_WEB_FETCH_RETRIES = 3
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.126 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    }

    html_content = ""
    last_exception = None
    is_first_attempt = True
    for _ in range(NUM_WEB_FETCH_RETRIES):
        request = None
        prepared_request = None

        if not is_first_attempt:
            LOGGER.debug("Backing off before attempting retry")
            time.sleep(10)
        else:
            is_first_attempt = False

        try:
            with suppress_warnings():
                LOGGER.debug(f"Requesting {url}")

                request = requests.Request(
                    method="GET",
                    url=url,
                    headers=headers,
                )

                prepared_request = request.prepare()

                with requests.Session() as session:
                    response = session.send(
                        prepared_request,
                        timeout=60,
                        verify=False,
                    )
        except Exception as e:
            last_exception = e
            LOGGER.warning(
                f"Recoverable exception (retrying) in _get_page_as_markdown while fetching {url}: {e}"
            )
            continue

        if not response:
            last_exception = requests.exceptions.RequestException(
                "No response",
                request=(prepared_request or request),
            )
            LOGGER.warning(f"No content retrieved from URL: {url}")
            continue

        if response.status_code != 200:
            errmsg = None
            try:
                errmsg = response.text()
            except Exception:
                pass

            LOGGER.warning(
                f"Fetch failed for URL: {url} Status code: {response.status_code} Message: {errmsg}"
            )
            last_exception = requests.exceptions.RequestException(
                errmsg,
                request=(prepared_request or request),
                response=response,
            )
            response = None
            continue

        if response:
            last_exception = None

            # Parse the content from the response.
            # With errors="ignore", it shouldn't throw.
            # If it does throw, we can go ahead and propagate it up.
            html_content = response.content.decode("utf-8", errors="ignore")
            break

    if not html_content:
        if last_exception:
            raise last_exception
        return ""

    return html_content


def _get_html_content_via_selenium(
    url: str,
    driver: webdriver.Chrome,
) -> str:
    LOGGER.debug(f"Fetching URL {url} with Selenium")
    driver.get(url)
    html_content = driver.page_source
    html_content = f"{html_content or ''}"
    return html_content


def _convert_html_to_markdown(
    html_content: str,
    url: str,
) -> str:
    try:
        # Get the site's presumed base URL from the URL itself.
        url_proto, url_therest = url.split("//")
        url_domain = url_therest.split("/")[0]
        base_url = f"{url_proto}//{url_domain}"
    except Exception:
        # Log the exception with traceback
        LOGGER.exception(
            f'Exception in _convert_html_to_markdown while trying to parse URL (string is not a valid URL): "{url}"'
        )
        return None

    # Look for an HTML tag to confirm that this is in fact HTML content.
    # Look for a <base> tag to get the base URL.
    # If it doesn't exist, just keep the base URL that was gleaned from the target URL.
    try:
        soup = BeautifulSoup(html_content, "html.parser")

        html_tag = soup.find("html")
        if not html_tag:
            LOGGER.warning(f"_get_page_as_markdown failed because no html tag in {url}")
            return None

        base_tag = soup.find("base")
        if base_tag:
            base_url = base_tag["href"]
    except Exception:
        # Log the exception with traceback
        LOGGER.exception(f"Exception in _get_page_as_markdown parsing HTML of {url}")
        return None

    html2text_markdown_converter.baseurl = base_url

    markdown_content = None
    NUM_PARSE_ATTEMPTS = 5
    for _ in range(NUM_PARSE_ATTEMPTS):
        # html2text_markdown_converter appears to be not entirely threadsafe.
        # If we fail to parse once, try again, just in case another thread was
        # clobbering us.
        try:
            markdown_content = html2text_markdown_converter.handle(html_content)
            break
        except Exception as e:
            # Log the exception with traceback
            LOGGER.warning(
                f"Retrying html2text_markdown_converter after exception in "
                f"_get_page_as_markdown converting HTML of {url}: {e}"
            )

    if not markdown_content:
        return None

    # We'll now strip lines and consolidate whitespace.
    lines = markdown_content.splitlines()
    lines = [line.strip() for line in lines]
    markdown_content = "\n".join(lines)
    markdown_content = re.sub(r"\n\n\n+", "\n\n", markdown_content)

    return markdown_content


def _call_gpt(
    conversation: Union[str, dict, List[dict]],
    openai_client: openai.OpenAI,
    *,
    json_format: str = "",
) -> Union[str, dict, list]:
    if isinstance(conversation, str):
        conversation = [{"role": "user", "content": conversation}]
    elif isinstance(conversation, dict):
        conversation = [conversation]

    conversation = json.loads(json.dumps(conversation))

    if json_format:
        conversation.append(
            {
                "role": "system",
                "content": (
                    "Structure your response as a JSON object. "
                    "Use the following format:\n\n"
                    f"{json_format}"
                ),
            }
        )

    answer_full = ""
    while True:
        LOGGER.debug(
            f"webpage2content._call_gpt calling chat completion "
            f"with conversation of {len(conversation)} messages. "
            f"Last message is {len(conversation[-1]['content'])} chars long."
        )

        completion = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation,
            temperature=0,
            response_format={"type": "json_object"} if json_format else None,
        )
        replystr = completion.choices[0].message.content

        if json_format:
            # We don't loop when we're doing json_format.
            replyobj: Union[dict, list] = json.loads(replystr)
            return replyobj

        answer_full += replystr + "\n"

        LOGGER.debug(
            f"webpage2content._call_gpt got answer of length {len(replystr)}, "
            f"appending to full answer currently at length {len(answer_full)}"
        )

        conversation.append(
            {
                "role": "assistant",
                "content": replystr,
            }
        )
        conversation.append(
            {
                "role": "user",
                "content": "Please continue from where you left off.",
            }
        )

        if completion.choices[0].finish_reason == "length":
            LOGGER.debug(
                "webpage2content._call_gpt finish reason length, continuing loop"
            )
            continue

        break

    answer_full = answer_full.strip()
    return answer_full


def check_human_readable(markdown: str, openai_client: openai.OpenAI) -> bool:
    try:
        # We should be able to see if it's human readable within the first 100,000 chars.
        conversation = [
            {"role": "system", "content": SYSTEMPROMPT},
            {"role": "user", "content": markdown[:100000]},
            {
                "role": "system",
                "content": "Does this look like human-readable content?",
            },
        ]
        gptreply_is_human_readable = _call_gpt(
            conversation=conversation,
            openai_client=openai_client,
            json_format="""
{
  "discussion": "...", # (str, freeform) What is this page? What's it for?
  "arguments_pro": "...", # (str, freeform) Offer some arguments for why this page might indeed be considered human-readable content.
  "arguments_con": "...", # (str, freeform) Offer some arguments for why this page might *not* be considered human-readable content.
  "argument_synthesis": "...", # (str, freeform) We've heard both sides: pro and con. Explain which side is more compelling.
  "is_human_readable": true/false # (bool) True if it's human-readable. False if not.
}
""",
        )
        if not gptreply_is_human_readable:
            LOGGER.warning("GPT returned no reply when determining human readability")
            return False

        if gptreply_is_human_readable.get("is_human_readable"):
            return True

        return False

    except Exception:
        LOGGER.exception("Exception in webpage2content checking human readability")
        return False


def get_page_description(markdown: str, url: str, openai_client: openai.OpenAI) -> str:
    description = ""
    # We should be able to get the gist within the first 100,000 chars.
    try:
        conversation = [
            {"role": "system", "content": SYSTEMPROMPT},
            {"role": "user", "content": f"URL: {url}"},
            {"role": "user", "content": markdown[:100000]},
            {
                "role": "system",
                "content": """
What is the purpose of this specific web page? What would a user come here to find?
Is there a single most important feature or topic, or is it more of a collection?
Look at the page's title, its headers, its body paragraphs, and so on.
Ignore boilerplate; ignore navigation links; ignore links to "related" articles
or "related" sites. What is *this* *specific* web page about?
""",
            },
        ]
        description = _call_gpt(
            conversation=conversation,
            openai_client=openai_client,
        )
        return description

    except Exception:
        LOGGER.exception("Exception in webpage2content getting page description")
        return ""


# We don't want to waste the LLM's time with blank lines, but we don't want to completely
# erase them either because they are sometimes useful for separating content.
# We'll store blank lines as newlines on the ends of existing lines.
# Each line object is a dict with the fields:
# - text
# - line_number (1-indexed)
# - is_pertinent (defaults to False)
def _enumerate_lines(markdown: str) -> List[dict]:
    mdlinetexts = [""]
    for line in markdown.splitlines():
        line = line.strip()
        if not line:
            # It's a blank line, which groups with the previous line.
            mdlinetexts[-1] += "\n"
        else:
            mdlinetexts.append(line)

    if not mdlinetexts[0].strip():
        # The first line is blank.
        mdlinetexts = mdlinetexts[1:]

    # Deliberately insert a blank line at the beginning to produce 1-indexing.
    # Yes, even if we possibly just removed one.
    mdlinetexts.insert(0, "")
    mdlines = [
        {
            "line_number": line_number,
            "text": text,
            "is_pertinent": False,
        }
        for line_number, text in enumerate(mdlinetexts)
    ]

    # And now remove the blank 0 line.
    mdlines = mdlines[1:]

    return mdlines


def _process_line_batch(
    page_description: str,
    line_number_batch_start: int,
    line_batch_size: int,
    mdlines: List[dict],
    openai_client: openai.OpenAI,
    *,
    url: str = "",
):
    LOGGER.debug(
        f"webpage2content processing URL {url} line batch "
        f"{line_number_batch_start}-{line_number_batch_start+line_batch_size-1} of {len(mdlines)}"
    )

    # We mitigate the threat of enormous markdowns on GPT's context window size,
    # by using a rolling line-numbered context window.
    # Build a context window. In case lines are too long, fiddle with cutoffs to
    # ensure that as much of our important lines make it into the consideration.
    # The context window will include 3 batches that come before our cared-about
    # lines, our cared-about lines, and then 1 batch after our cared-about lines.
    mdtexts_before = [
        f"{l['line_number']}. {l['text']}"
        for l in mdlines
        if l["line_number"] >= (line_number_batch_start - (3 * line_batch_size))
        and l["line_number"] < line_number_batch_start
    ]
    mdtext_before = "\n".join(mdtexts_before)
    mdtext_before = mdtext_before[:50000]

    mdtexts_careabout = [
        f"{l['line_number']}. {l['text']}"
        for l in mdlines
        if l["line_number"] >= line_number_batch_start
        and l["line_number"] < (line_number_batch_start + line_batch_size)
    ]
    mdtext_careabout = "\n".join(mdtexts_careabout)
    mdtext_careabout = mdtext_careabout[:50000]

    mdtexts_after = [
        f"{l['line_number']}. {l['text']}"
        for l in mdlines
        if l["line_number"] >= (line_number_batch_start + line_batch_size)
        and l["line_number"] < (line_number_batch_start + (2 * line_batch_size))
    ]
    mdtext_after = "\n".join(mdtexts_after)
    mdtext_after = mdtext_after[:50000]

    mdtext_context_window = f"{mdtext_before}\n{mdtext_careabout}\n{mdtext_after}"

    conversation = [
        {
            "role": "system",
            "content": (
                f"{SYSTEMPROMPT}\n\n"
                "I've annotated the markdown with line numbers.\n\n"
                "NOTE: For very large pages, I might abridge the content, but I'll "
                "provide you with enough context to make intelligent decisions."
            ),
        },
        {"role": "user", "content": mdtext_context_window},
        {
            "role": "system",
            "content": "Describe this page. What is its main purpose or topic?",
        },
        {"role": "assistant", "content": page_description},
        {
            "role": "system",
            "content": (
                "Is every line relevant to this page's purpose or topic? "
                "More specifically, if a human user were to come to this page with the intent "
                "of learning information (i.e. about the page's purpose or topic), would "
                "every line be of interest to such a user?"
            ),
        },
        {"role": "assistant", "content": INVPROMPT_NOT_EVERY_LINE_RELEVANT},
        {
            "role": "system",
            "content": (
                "For the current task, I'd like you to focus your attention specifically "
                f"on lines {line_number_batch_start} "
                f"through {line_number_batch_start + line_batch_size - 1}. "
                "I want you to go through these lines one by one. For each one, make a judgment "
                "about whether or not that specific line contains readable content that would be "
                "relevant to a human visitor. Remember, you've already discerned this page's "
                "main purpose or topic. The human visitor is here because they want information "
                "about the main purpose or topic that you identified above (I'll repeat it below). "
                "Any line that isn't pertinent to this page's main purpose or topic should be removed. "
            ),
        },
    ]

    line_judgments_obj = _call_gpt(
        conversation=conversation,
        openai_client=openai_client,
        json_format="""
{
  "line_judgments": [
    {
      "line_number": n, # (int) The line number.
      "category": "...", # (str) A very brief statement of what kind of line this is. Is it a title? An ad? A navigation link? A descriptive paragraph?
      "relation_to_page_purpose": "...", # (str) A very brief statement explaining how (or *if*) this line relates to the page's main purpose or topic.
            # If it does indeed relate, explain why you think so.
      "is_pertinent": true/false # (bool) Is this line pertinent to the page's main purpose or topic?
    },
    ...
  ]
}
""",
    )

    if not line_judgments_obj or "line_judgments" not in line_judgments_obj:
        LOGGER.warning(
            f"GPT couldn't judge line batch starting at {line_number_batch_start}"
        )
        return

    line_judgments: List[dict] = line_judgments_obj["line_judgments"]
    for line_judgment in line_judgments:
        line_number = line_judgment.get("line_number")
        if not line_number:
            continue
        line_objs_matching = [l for l in mdlines if l["line_number"] == line_number]
        if len(line_objs_matching) == 0:
            continue
        line_obj = line_objs_matching[0]
        if line_judgment.get("is_pertinent"):
            line_obj["is_pertinent"] = True

    num_lines_kept = len([l for l in line_judgments if l.get("is_pertinent")])
    LOGGER.debug(
        f"webpage2content processed URL {url} line batch "
        f"{line_number_batch_start}-{line_number_batch_start+line_batch_size-1} of {len(mdlines)}, "
        f"kept {num_lines_kept} lines out of {len(line_judgments)}"
    )

    return


def webpage2content(
    url: str,
    openai_client: openai.OpenAI,
    *,
    attempt_with_requests: bool = True,
    attempt_with_selenium: bool = False,
    prefer_selenium: bool = False,
    selenium_page_load_wait_seconds: Optional[int] = None,
    selenium_driver: Optional[webdriver.Chrome] = None,
):
    ts_start = time.time()

    # Sanity-check arguments

    if not attempt_with_requests and not attempt_with_selenium:
        raise ValueError(
            "You must specify at least one: attempt_with_requests, attempt_with_selenium"
        )

    if prefer_selenium and not attempt_with_selenium:
        raise ValueError(
            "You can't specify prefer_selenium=True with attempt_with_selenium=False"
        )

    if attempt_with_selenium and (selenium_driver is None):
        raise ValueError(
            "To attempt with Selenium, you need to pass in a Selenium driver. "
            "Create one with this module's create_selenium_driver method."
        )

    if selenium_page_load_wait_seconds is not None:
        if not attempt_with_selenium:
            raise ValueError(
                f"You've told Selenium to wait for {selenium_page_load_wait_seconds} seconds, "
                "but you've also specified to not use Selenium. Make up your mind!"
            )
        selenium_driver.implicitly_wait(selenium_page_load_wait_seconds)

    # Sanity-check the URL

    if type(url) != str:
        LOGGER.warning("webpage2content got a URL that isn't a string.")
        return None

    url = url.strip()
    if not url:
        LOGGER.warning("webpage2content got empty URL.")
        return None

    url = f"{url}"
    url = _remove_double_slashes(url)

    # Attempt to get page contents.

    html_content = ""

    if attempt_with_requests and not attempt_with_selenium:
        html_content = _get_html_content_via_requests(url)

    elif attempt_with_selenium and not attempt_with_requests:
        html_content = _get_html_content_via_selenium(url, selenium_driver)

    elif prefer_selenium:
        try:
            html_content = _get_html_content_via_selenium(url, selenium_driver)
        except Exception as e:
            LOGGER.warning(
                f"Got exception with Selenium (falling back on requests). {e}"
            )

        if not html_content:
            html_content = _get_html_content_via_requests(url)

    else:
        try:
            html_content = _get_html_content_via_requests(url)
        except Exception as e:
            LOGGER.warning(
                f"Got exception with requests (falling back on Selenium). {e}"
            )

        if not html_content:
            html_content = _get_html_content_via_selenium(url, selenium_driver)

    if not html_content:
        return ""

    # We've finally gotten HTML content.
    # Now convert it to Markdown, because it's easier for the LLM to handle.

    markdown = _convert_html_to_markdown(
        html_content=html_content,
        url=url,
    )
    if not markdown:
        return None

    if not isinstance(markdown, str):
        LOGGER.error("markdown somehow came back as something other than a string.")
        return None

    markdown = markdown.strip()
    if not markdown:
        return None

    is_human_readable = check_human_readable(markdown, openai_client)
    if not is_human_readable:
        LOGGER.warning(f"Page at {url} is not human-readable")
        return None

    page_description = get_page_description(markdown, url, openai_client)

    mdlines = _enumerate_lines(markdown)

    max_line_number = max(l["line_number"] for l in mdlines)

    LOGGER.debug(
        f"webpage2content reading {max_line_number} lines from {url} -- {page_description}"
    )

    LINE_BATCH_SIZE = 100

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for line_number_batch_start in range(1, max_line_number + 1, LINE_BATCH_SIZE):
            future = executor.submit(
                _process_line_batch,
                page_description=page_description,
                line_number_batch_start=line_number_batch_start,
                line_batch_size=LINE_BATCH_SIZE,
                mdlines=mdlines,
                openai_client=openai_client,
                url=url,
            )
            futures.append(future)

        # Wait for all futures to complete.
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                # Handle exceptions if any occurred during processing
                LOGGER.exception(
                    f"webpage2content encountered an error during concurrent line batch processing: {e}"
                )

    retval_texts = [
        (l.get("text") or "").strip() for l in mdlines if l.get("is_pertinent")
    ]
    LOGGER.debug(
        f"webpage2content URL {url} line count before filter: {len(mdlines)} After filter: {len(retval_texts)}"
    )
    retval = "\n".join(retval_texts)

    # The most consecutive newlines we allow is 2, i.e. 1 blank line.
    # Replace all occurrences of >2 newlines in a row with 2 newlines.
    retval = re.sub(r"\n{3,}", "\n\n", retval)
    retval = retval.strip()

    LOGGER.debug(
        f"webpage2content finished URL {url}, "
        f"a page with {max_line_number} lines of Markdown, "
        f"in {time.time() - ts_start} sec"
    )

    return retval


def main():
    import argparse
    import dotenv
    import os

    # Read the version from the VERSION file
    with open(os.path.join(os.path.dirname(__file__), "VERSION"), "r") as version_file:
        version = version_file.read().strip()

    parser = argparse.ArgumentParser(
        description=(
            "A simple Python package that takes a web page (by URL) and extracts its "
            "main human-readable content. It uses LLM technology to remove all of the "
            "boilerplate webpage cruft (headers, footers, copyright and accessibility "
            "notices, advertisements, login and search controls, etc.) that isn't part "
            "of the main content of the page."
        )
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {version}",
        help="Show the version number and exit.",
    )

    parser.add_argument(
        "-l",
        "--log-level",
        help="Sets the logging level. (default: %(default)s)",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )

    parser.add_argument(
        "-u",
        "--url",
        help="The URL to read.",
        type=str,
    )
    parser.add_argument(
        "url_arg",
        help="Same as --url, but specified positionally.",
        type=str,
        nargs="?",
    )

    parser.add_argument(
        "-k",
        "--key",
        help="OpenAI API key. If not specified, reads from the environment variable OPENAI_API_KEY.",
        type=str,
        default="",
    )
    parser.add_argument(
        "key_arg",
        help="Same as --key, but specified positionally.",
        type=str,
        nargs="?",
    )

    parser.add_argument(
        "-o",
        "--org",
        help="OpenAI organization ID. If not specified, reads from the environment variable OPENAI_ORGANIZATION. "
        "If no such variable exists, then organization is not used when calling the OpenAI API.",
        type=str,
        default="",
    )
    parser.add_argument(
        "org_arg",
        help="Same as --org, but specified positionally.",
        type=str,
        nargs="?",
    )

    parser.add_argument(
        "--selenium-chrome-binary",
        help="Full path of the Chrome binary, if you want to use Selenium.",
        type=str,
        required=False,
        default="",
    )

    parser.add_argument(
        "--selenium-chromedriver-binary",
        help="Full path of the chromedriver binary, if you want to use Selenium.",
        type=str,
        required=False,
        default="",
    )

    parser.add_argument(
        "--selenium-page-load-wait-seconds",
        help="How many seconds Selenium spends waiting for a page to populate with content.",
        type=int,
        required=False,
    )

    parser.add_argument(
        "--selenium-preferred",
        help="Flag that says to try Selenium first, *then* requests.",
        action="store_true",
        default=False,
    )

    args = parser.parse_args()

    if args.log_level:
        log_level = logging.getLevelName(args.log_level)
        LOGGER.setLevel(log_level)
        _LOGGING_CONSOLE_HANDLER.setLevel(log_level)

    dotenv.load_dotenv()

    openai_api_key = args.key or args.key_arg or os.getenv("OPENAI_API_KEY")
    openai_org_id = args.org or args.org_arg or os.getenv("OPENAI_ORGANIZATION_ID")
    url = args.url or args.url_arg

    if not url:
        parser.error("URL is required.")
    if not openai_api_key:
        parser.error("OpenAI API key is required.")

    openai_client = openai.OpenAI(api_key=openai_api_key, organization=openai_org_id)

    selenium_driver = None
    if (
        args.selenium_chrome_binary
        or args.selenium_chromedriver_binary
        or args.selenium_page_load_wait_seconds
        or args.selenium_preferred
    ):
        if not args.selenium_chrome_binary or not args.selenium_chromedriver_binary:
            raise ValueError(
                "You must specify both selenium-chrome-binary and selenium-chromedriver-binary "
                "in order to use Selenium."
            )
        selenium_driver = create_selenium_driver(
            chrome_binary_location=args.selenium_chrome_binary,
            chromedriver_binary_location=args.selenium_chromedriver_binary,
        )

    s = webpage2content(
        url=url,
        openai_client=openai_client,
        attempt_with_selenium=(selenium_driver is not None),
        selenium_driver=selenium_driver,
        prefer_selenium=args.selenium_preferred,
        selenium_page_load_wait_seconds=args.selenium_page_load_wait_seconds,
    )
    print(s)


if __name__ == "__main__":
    main()

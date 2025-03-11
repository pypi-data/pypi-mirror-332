from .webpage2content_impl import webpage2content
from .webpage2content_impl import create_selenium_driver
from .webpage2content_impl import check_human_readable

# Apparently, you're not supposed to make the module callable.
# A thing that you do all the time in NodeJS is apparently a huuuuuuuge no-no
# in Python.
# https://stackoverflow.com/questions/56387636/how-to-create-a-python-module-as-a-single-callable-function

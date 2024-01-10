#!/usr/bin/python3
"""
function that appends a string at the end of function that appends a string
at the end of a text file (UTF8) and returns the numberof characters added:
ext file (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    This function Appends a string at the end of a text file (utf8)
    and return the number of charcters added.

    Args:
        filename (str): The name of the file.
        text (str): The text to be append  to the file.
    Returns:
        the number of the charcters added.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)

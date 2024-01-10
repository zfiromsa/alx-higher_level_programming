#!/usr/bin/python3
"""
Module with append_Write function.
"""

def append_Write(filename="", text=""):
    """
    Appends a string at the end of a text file (utf8)
    and return the number of charcters added.

    Args:
        filename (str): The name of the file.
        text (str): The text to be append  to the file.
    Returns:
        int: the number of the charcters added.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)

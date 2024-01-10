#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout:"""

def read_file(filename=""):
    """
    This function read a test file (utf8) and print it to stdout.
    Args:
        filename (str): the name of the file to be read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())

#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""
def write_file(filename="", text=""):
    """
    This a function that writes a string to a text file (UTF8)
    and returns the number of characters written:

    Args:
        filename (str): the name of a file to be wriiten.
        test (str): the text to be written to the file
    Returns:
        Number of charcters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

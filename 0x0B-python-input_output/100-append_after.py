#!/usr/bin/python3
"""
THIS function that inserts a line of text to a file, after each
line containing a specific string (see example):
"""


def append_after(filename="", search_string="", new_string=""):
    """"
    Insert a line of text a file  after each line containing a specific string.

    Args:
        filename (str): the name of the file.
        search_string (str): The specific string to search for in each line.
        new_string (str): The line of text to inser after  each line containing
        the search string.  
    """"
    with open(filename, 'r', encoding='utf-8') as f:
        lines =f.readlines()

    with open(filename, 'W', encoding="utf-8") as file:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')

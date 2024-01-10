#!/usr/bin/python3
"""
This function that inserts a line of text to a file, after each line contain
"""


def append_after(filename="", search_string="", new_string=""):
    """"
    Insert a line of text a file  after each line containing
    a specific string.

    Args:
        filename (str): the name of the file.
        search_string (str): The specific string to search for in each line.
        new_string (str): The line of text to inser after  each line contain
        the search string.  
    """"
    # Read the content of the file into a list of lines
    with open(filename, 'r', encoding='utf-8') as f:
        lines =f.readlines()
    # Open the file in Write mode
    with open(filename, 'W', encoding="utf-8") as f:
        for line in lines:
            # Write each line to the file
            f.write(line)

            #If the search string is found in 
            if search_string in line:
                f.write(new_string + '\n')

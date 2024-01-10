#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
and returns the number of characters written:
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

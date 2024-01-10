#!/usr/bin/python3
""""Import json modul"""
import json
"""
This a function that creates an Object from a “JSON file”:
"""


def load_from_json_file(filename):
    """
    Write an object to a text file using a json representation.

    Args:
        filename (str): the name of the file to be saved the json represent.
    Return:
        obj: the python object created the Json fole.
    """

    with open(filename, mode="r", encoding='utf-8') as f:
        return json.load(f)

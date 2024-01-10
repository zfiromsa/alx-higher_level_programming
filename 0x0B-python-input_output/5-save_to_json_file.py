#!/usr/bin/python3
""""Import json modul"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a json representation.

    Args:
        my_obj: the python object to be serialized  and saved.
        filename (str): the name of the file to be saved the json representtation
    """

    with open(filename, mode="w", encoding='utf-8') as f:
        json.dump(my_obj, f)

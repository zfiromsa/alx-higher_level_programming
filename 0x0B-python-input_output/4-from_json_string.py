#!/usr/bin/python3
""""Import json modul"""
import json

""""
function that returns an object (Python data structure) represented by a JSON string:
"""


def from_json_string(my_str):
    """"
    Return an object (python data structure) represened by a Json string.

    Args:
        my_str (str):  the json string to be converted to a python object.

    Returns:
        obj: the python object represented by the json string.
    """
    return json.loads(my_str)

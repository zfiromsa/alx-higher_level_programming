#!/usr/bin/python3
"""Returns the JSON  reepresent of an object (string)."""
import json

"""Returns the JSON  reepresent of an object (string)."""
def to_json_string(my_obj):
    """
    Args:
        my_obj: The object to be converted to a json string.
    Returns:
        str: The Json representation of the obj
    """
    return json.dumps(my_obj)

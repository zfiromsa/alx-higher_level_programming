#!/usr/bin/python3
"""
Aa func that returns the list of available attribut and methods of an obj:
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to lookup.

    Returns:
        list: A list of available attributes and methods of the object.
    """
    attributes_and_methods = []
    for item in dir(obj):
        if callable(getattr(obj, item)):
            attributes_and_methods.append(item + '()')
        else:
            attributes_and_methods.append(item)
    return attributes_and_methods

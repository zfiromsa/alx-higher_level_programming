#!/usr/bin/python3
"""
a function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the
specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Return true or false depend object is an instance

    Args:
        obj: object.
        a_class: class.
    Returns:
        boolean value true or false.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

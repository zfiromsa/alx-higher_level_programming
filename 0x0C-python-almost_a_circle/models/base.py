#!/usr/bin/python3
"""
This module provides the main script for the Rectangle program.
It creates two rectangle instances, displays them, and 
updates the second one before displaying it again.
"""


class Base:
    """Private class attribute"""
    __nb_objects = 0

    """

    """
    def __init__(self, id=None):
        """
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

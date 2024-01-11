#!/usr/bin/python3
"""
It is an Empty class
"""


class BaseGeometry:
    """Empty class for representing base geometry."""

    def area(self):
        """
        Raises an Exception with the mesage 'area() is not implemented'

        Raises:
            Exception: Always raises an exception.
        """
        raise Exception("area() is not implemented")

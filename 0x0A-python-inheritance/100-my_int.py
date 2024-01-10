#!/usr/bin/python3
"""
Write a class MyInt that inherits from int:

MyInt is a rebel. MyInt has == and != operators inverted
You are not allowed to import any module
"""
class MyInt(int):
    """
    A custom integer class that inherits from the built-in int class,
    but has the == and != operators inverted.
    """

    def __eq__(self, other):
        """
        Override the == operator to return the inverted result of the != operator.
        Args:
            other (Any): The value to compare with.
        Returns:
            bool: True if not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to return the inverted result of the == operator.
        Args:
            other (Any): The value to compare with.
        Returns:
            bool: True if equal, False otherwise.
        """
        return super().__eq__(other)

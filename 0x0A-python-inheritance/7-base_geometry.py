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

    def integer_validator(self, name, value):
        """
        Validates the value to be an integer greater than 0.

        Args:
        name (str): The name of the value.
        Value: the value to be validated.

        Raises:
            TypeError: If he value is not an integer.
            ValueError: If the value is less than or equel to 0.
        """
        if not isinstance(value, int):
            raise TypeErro(f"{name}must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name}must be greater than 0")

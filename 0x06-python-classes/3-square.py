#!/usr/bin/python3
"""
a class Square that defines a square
"""


class Square:
    """
    A class that defines a square by its size.

    Attrirbutes:
    size (int): size of a the square

    Methods:
    None for now.
    """
    def __init__(self, size=0):
        """
        Constructs a new instance of the squere class.

        parameters:
        size (int): the size of a side of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """
        Return the current square area.

        Returns:
            int the area of the squre
        """
        return self.__size ** 2

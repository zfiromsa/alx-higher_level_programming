#!/usr/bin/python3
"""
A class Square that defines a square
"""


class Square:
    """
    A class that defines a square by its size.

    Attrirbutes:
    size (int): size of a the square

    Methods:
    None for now.
    """
    def __init__(self, size):
        """
        Constructs a new instance of the squere class.

        parameters:
        size (int): the size of a side of the square
        """
        self.__size = size

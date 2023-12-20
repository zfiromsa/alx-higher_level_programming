#!/usr/bin/python3
class Square:
    """
    A class to represent a square.

    ...
    Attributes
    ---------
    __size : int
        private  attribute to keep trak of the size of square
    Methods
    --------
    size(self):
        gets the value of __size
    size(self, value):
        sets the value of __size
    area(self):
        calculate the area of the squer
    """

    def __init__(self, size=0):
        """
        constructs all the necessar atttributes for the squeare object.

        parameters
        -------
        size : int, optional
            size of the square (default is 0)
        """
        self.size = size
    @property
    def size(self):
        """
        Returns
        ------
            int
                size of the square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        sets the value of __size.
        parameters
        --------
            value : int
                size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an intger")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
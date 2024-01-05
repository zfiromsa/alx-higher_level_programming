#!/usr/bin/python3
"""
This is a module for defining a Rectangle class.
"""

class  Rectangle:
    """
    This is a Rectangle CLASS.
    It current doesn't have any attributes or methodes.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        :param width: the width of rectangle. Default to 0.
        :param height: the height of rectangle. Default to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of Rectangle

        :param value: The new width of the reactangle.
        :raises TypeError: If the width is not an integer
        :raises ValueError: If the width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of Rectangle

        :param value: The new height of the reactangle.
        :raises TypeError: If the height is not an integer
        :raises ValueError: If the height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of Rectangle and Return area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate the perimeter of Rectangle and Return perimeter of rectangle

        :return: The perimet of rect or 0 if either the width or heighr is 0.
        """
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

#!/usr/bin/python3
class Rectangle:
    """A Class Rectangle defines a rectangle."""

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
        return self.width

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
        return self.height
 
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

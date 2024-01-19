#!/usr/bin/python3
""" Import Bsae from base"""
from models.base import Base

"""
The rectangle module defines the rectangle class.
"""


class Rectangle(Base):
    """
    The rectangle class definesa rectangle shape.

    Attributes:
    width: the width of the rectangle.
    height: the height of the rectangle.
    x: the x-cordinate of the rectangle
    y: the y-cordinate of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Reactangle instance.

        parameters:
            width: the width of the rectangle.
            height: the height of the rectangle.
            x: the x-cordinate of the rectangle
            y: the y-cordinate of the rectangle
            id: An optional Id 
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns: the width of the rectanle.
        """
        return self.__width

    @property
    def y(self):
        """
        Get the y-cordinate of the rectangle.

        Returns: the y-cordinate of the rectanle.
        """
        return self.__y

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns: the height of the rectanle.
        """
        return self.__height

    @property
    def x(self):
        """
        Get the x-cordinate of the rectangle.

        Returns: the x-cordinate of the rectanle.
        """
        return self.__x

    @width.setter
    def width(self, value):
        """
        set the width of the rectangle.

        parameters:
            value: the new width of the rectangle.
        raises:
            valueError: if the provided value is not int or float
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    
    @height.setter
    def height(self, value):
        """
        set the heihgt of the rectangle.

        parameters:
            value: the new height of the rectangle.
        raises:
            valueError: if the provided value is not int or float
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @x.setter
    def x(self, value):
        """
        set the x-cordinate of the rectangle.

        parameters:
            value: the new x-coordinate of the rectangle.
        raises:
            valueError: if the provided value is not int or float
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @y.setter
    def y(self, value):
        """
        set the y-cordinate of the rectangle.

        parameters:
            value: the new y-coordinate of the rectangle.
        raises:
            valueError: if the provided value is not int or float
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This mudels calculate the area of a rectangle.

        Returns: the area value of the Rectangle instance.
        """
        return self.__height * self.__width
    
    def __str__(self) -> str:
        return f"[Rectangle] ({self.id}/{self.x} - {self.width}/{self.height})"
    def display(self):
        """
        This models prints in stdout the Rectangle instance 
        with the character # 
        """
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()
    def update(self, *args, **kwargs):
        """
        This models that assigns an argument to each attribute
        """
        if args:
            args_l = ["id", "width", "height", "x", "y"]
            for i , value in enumerate(args_l):
                setattr(self, args_l[i], value)

        elif kwargs:
            if "id" in kwargs:
                self.__id = kwargs["id"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]


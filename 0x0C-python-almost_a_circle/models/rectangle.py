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
        def Width(self):
            """
            Get the width of the rectangle.

            Returns: the width of the rectanle.
            """
            return self.__width
        
        @Width.setter
        def width(self, value):
            """
            set the width of the rectangle.

            parameters:
                value: the new width of the rectangle.
            raises:
                valueError: if the provided value is not int or float
            """
            if isinstance(value, (int, float)):
                self.__width = value
            else:
                raise ValueError("Width must be an integer")
            
        @property
        def height(self):
            """
            Get the height of the rectangle.

            Returns: the height of the rectanle.
            """
            return self.__height
        
        @height.setter
        def set_height(self, value):
            """
            set the heihgt of the rectangle.

            parameters:
                value: the new height of the rectangle.
            raises:
                valueError: if the provided value is not int or float
            """
            if isinstance(value, (int, float)):
                self.__height = value
            else:
                raise ValueError("Height must be an integer")

        @property
        def x(self):
            """
            Get the x-cordinate of the rectangle.

            Returns: the x-cordinate of the rectanle.
            """
            return self.__width
        
        @x.setter
        def set_x(self, value):
            """
            set the x-cordinate of the rectangle.

            parameters:
                value: the new x-coordinate of the rectangle.
            raises:
                valueError: if the provided value is not int or float
            """
            if isinstance(value, int):
                if value < 0:
                    raise ValueError("x must be >= 0")
                self.__x = value
            else:
                raise ValueError("x must be an integer")
                
        @property
        def y(self):
            """
            Get the y-cordinate of the rectangle.

            Returns: the y-cordinate of the rectanle.
            """
            return self.__y
        
        @y.setter
        def set_y(self, value):
            """
            set the y-cordinate of the rectangle.

            parameters:
                value: the new y-coordinate of the rectangle.
            raises:
                valueError: if the provided value is not int or float
            """
            if isinstance(value, int):
                if value < 0:
                    raise ValueError("y must be >= 0")
                self.__y = value
            else:
                raise ValueError("y must be an integer")
            
            def area(self):
                return self.__height * self.__width
            
            def display(self):
                for k in range(self.__y):
                    print()
                for i in range(self.__height):
                    for l in range(self.__x):
                        print(" ", end="")
                    for j in range(self.__width):
                        print("#", end="")
                    print()
            def update(self, *args, **kwargs):
                if len(args) > 0:
                    if len(args) >= 1:
                        self.__id = args[0]
                    if len(args) >= 2:
                        self.__id = args[1]
                    if len(args) >= 3:
                        self.__id = args[2]
                    if len(args) >= 4:
                        self.__id = args[3]
                    if len(args) >= 5:
                        self.__id = args[4]

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
 
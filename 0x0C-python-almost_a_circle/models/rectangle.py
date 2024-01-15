#!/usr/bin/python3
"""
The rectangle module defines the rectangle class.
"""
from module.base import Base

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
        self.__height == height
        self.__x = x
        self.__y = y

        def get_Width(self):
            """
            Get the width of the rectangle.

            Returns: the width of the rectanle.
            """
            return self.__width
        
        def set_width(self, value):
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
            
        def get_height(self):
            """
            Get the height of the rectangle.

            Returns: the height of the rectanle.
            """
            return self.__height
        
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

        def get_x(self):
            """
            Get the x-cordinate of the rectangle.

            Returns: the x-cordinate of the rectanle.
            """
            return self.__width
        
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
                
            
        def get_y(self):
            """
            Get the y-cordinate of the rectangle.

            Returns: the y-cordinate of the rectanle.
            """
            return self.__y
        
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
                for i in range(self.__height):
                    for j in range(self.__width):
                        print("#", end="")
                    print()
 
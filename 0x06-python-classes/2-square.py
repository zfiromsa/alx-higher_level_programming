#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size_set(size)
    def size_set(self, size):
        if self.__size is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
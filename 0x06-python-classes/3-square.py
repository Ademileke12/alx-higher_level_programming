#!/usr/bin/python3
"""
This is the module for Squre below
"""

class Square:
    """ This is the implementation for the area"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        area = (self.__size) ** 2
        return area

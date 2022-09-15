#!/usr/bin/python3#!/usr/bin/python3
""" This module is the square class
"""


class Square:
    """The class implementation"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")

#!/usr/bin/python3
""" Square """
class Square:
    """ Defines a square"""
    def __init__(self, size=0):
        """Initializes and sets size to zero"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

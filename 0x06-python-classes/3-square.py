#!/usr/bin/python3
"""Area """
class Square(object):
    """ Defines class size"""
    def __init__(self, size=0):
        """Initialize """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates area"""
        return self.__size * self.__size

#!/usr/bin/python3
""" Simple Rectangle"""


class Rectangle:
    """ Define a rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ The width"""
	return self.__width

    @width.setter
    def width(self, value):
        """ Set the value width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Height function """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the value height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

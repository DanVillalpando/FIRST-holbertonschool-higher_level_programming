#!/usr/bin/python3
"""Access and update """


class Square(object):
    """class size"""
    def __init__(self, size=0):
        """initialize size"""
        self.__size = size

    @property
    def size(self):
        """Property """
        return self.__size

    @size.setter
    def size(self, value):
        """clss size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area"""
        return self.__size * self.__size

    def my_print(self):
        """ Prints #"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()

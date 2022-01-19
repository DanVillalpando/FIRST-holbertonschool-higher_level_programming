#!/usr/bin/python3
"""Access and update """


class Square(object):
    """class size"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize size"""
        self.__size = size
	self.position = position

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
        else:
            for i in range(0, self.__position[1]):
                print()
            for k in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
    @property
        def position(self):
        """ Position of square """
        return self.__position
    if type(value) != 

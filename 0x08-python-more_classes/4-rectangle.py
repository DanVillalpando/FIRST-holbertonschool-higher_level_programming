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

    def area(self):
        """ Calculates the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ 
	Calculate the perimeter of the rectangle
	"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2
        return(perimeter)
    
    def __str__(self):
        """
        print the rectangle
        with '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        new = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                new += "#"
            if i != (self.__height - 1):
                new += '\n'
        return new
    
    def __repr__(self):
        """
        string representation of the rectangle
        
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

#!/usr/bin/python3
"""
2. First Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """
	Calling the super class with id
        """
        super().__init__(id)

    def __str__(self):
        """
	prints information
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    @property
    def width(self):
        """
	Getter of value width
	"""
        return self.__width

    @width.setter
    def width(self, width):
        """
	Setter of the value width
	"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
	Getter of the height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
	Setter of the height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
	Getter of x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
	Setter of x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
	Getter of y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
	Setter of y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
	Returns area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
	Prints in stdout the Rectangle instance with the character #
        """
        for row in range(self.__y):
            print()

        for colum in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
	function that assigns a key/value argument to attributes:
        - 1st argument should be the id attribute
        - 2nd argument should be the width attribute
        - 3rd argument should be the height attribute
        - 4th argument should be the x attribute
        - 5th argument should be the y attribute
        """
        if args != ():
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if len(args) == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
	"""
	uptdate
	"""
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

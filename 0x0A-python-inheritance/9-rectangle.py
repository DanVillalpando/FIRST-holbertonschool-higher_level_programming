#!/usr/bin/python3
""" 9. Full rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits
    from BaseGeometry
    """

    def __init__(self, width, height):
        """
        private attributes width and height,
        must be positive integers.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Area of the recantgle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        print string rectangle description
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)

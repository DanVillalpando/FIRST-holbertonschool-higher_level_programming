#!/usr/bin/python3
""" 7. Integer validator """


class BaseGeometry:
    """ class BaseGeometry (based on 6-base_geometry.py)"""

    def area(self):
        """Public instance method and message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method, message n validate"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

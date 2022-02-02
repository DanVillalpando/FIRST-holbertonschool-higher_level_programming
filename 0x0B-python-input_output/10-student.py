#!/usr/bin/python3
"""
10. Student to JSON with filter
"""


class Student(object):
    """ class Student that defines a student """
    def __init__(self, first_name, last_name, age):
        """
	Public instance attributes:
	first_name
	last_name
	age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
	retrieves a dictionary representation
	of a Student instance
	"""
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
	return(self.__dict__)

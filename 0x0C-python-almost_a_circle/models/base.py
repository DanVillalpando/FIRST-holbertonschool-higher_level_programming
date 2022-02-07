#!/usr/bin/python3
"""
1. Base class
"""
import json


class Base:
    """ First class Base """
    __nb_objects = 0

    """
    private class attribute 
    __nb_objects
    """
    def __init__(self, id=None):
        """ init function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

                @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        new_list = []
        with open(cls.__name__ + ".json", "w", encoding="UTF-8") as f:
            if list_objs is not None:
                for x in list_objs:
                    lst.append(x.to_dictionary())
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):

        """
	returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

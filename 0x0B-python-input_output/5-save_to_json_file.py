#!/usr/bin/python3
"""
5. Save Object to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, "w", encoding="UTF_8") as MyFile:
        json.dump(my_obj, MyFile)
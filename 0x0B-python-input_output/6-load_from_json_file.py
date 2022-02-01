#!/usr/bin/python3
"""
6. Create object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”
    """
    with open(filename) as MyFyle:
        return (json.load(MyFile))

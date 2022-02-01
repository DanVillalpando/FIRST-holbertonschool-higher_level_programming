#!/usr/bin/python3
"""
2. Append to a file
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end o a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, "a", encoding='utf-8') as MyFile:
        return (MyFile.write(text))

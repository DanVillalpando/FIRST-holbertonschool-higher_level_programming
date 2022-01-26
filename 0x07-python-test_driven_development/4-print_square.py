#!/usr/bin/python3
""" 3. Print square """
def print_square(size):
    """ Prints a square 
    
    Using #
    
    """
    if type(size) is not int:
        raise ValueError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()

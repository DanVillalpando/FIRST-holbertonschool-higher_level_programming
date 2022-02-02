#!/usr/bin/python3
"""
12. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    elem = []
    lst = []
    for x in range(n):
        row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                row.append(1)
            else:
                row.append(lst[y] + lst[y - 1])
        lst = row
        elem.append(row)
    return elem

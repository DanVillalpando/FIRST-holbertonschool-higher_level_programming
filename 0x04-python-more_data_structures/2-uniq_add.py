#!/usr/bin/python3

def uniq_add(my_list=[]):
    empty = set()
    if my_list:
        for i in my_list:
            empty.add(i)
    return sum(empty)

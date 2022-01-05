#!/usr/bin/python3

def max_integer(my_list=[]):
    elements = len(my_list)
    if elements == 0:
        print("None")
    greater_n = my_list[0]
    for i in my_list:
        if i > greater_n:
            greater_n = i
    return greater_n

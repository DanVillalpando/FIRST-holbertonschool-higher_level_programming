#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new = my_list.copy()
    for k in range(len(new)):
        if new[k] % 2 == 0:
            new[k] = True
        else:
            new[k] = False
    return new

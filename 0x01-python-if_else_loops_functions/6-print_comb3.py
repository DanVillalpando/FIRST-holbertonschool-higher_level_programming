#!/usr/bin/python3
for n in range(10):
    for n2 in range(n + 1, 10):
        if n == 8 and n2 == 9:
            print("{:d}{:d}".format(n, n2))
        else:
            print("{:d}{:d}, ".format(n, n2), end="")

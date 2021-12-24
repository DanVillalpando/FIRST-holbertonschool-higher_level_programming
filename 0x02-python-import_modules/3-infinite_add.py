#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    suma = 0
    for i in range(len(sys.argv) - 1):
        suma += int(sys.argv[i + 1])
    print("{}".format(suma))

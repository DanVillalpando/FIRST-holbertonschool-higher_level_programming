#!/usr/bin/python3
""" 4. Text indentation """

def text_indentation(text):
    """ function that prints a text 
    with 2 new lines after each of these characters: 
    . ? and :     
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new = ""
    i = 0

    while i < len(text):
        if text[i] != "." and text[i] != "?" and text[i] != ":":
            new += text[i]
        else:
            new += text[i]
            print(new)
            print()
            new = ""
            while i < (len(text) - 1) and text[i+1] == " ":
                i += 1
        i += 1
    print(new, end="")


    for x in text:
        if x == '.' or x == '?' or x == ':':
            new += "\n\n"
        else:
            new += x
    print(new)

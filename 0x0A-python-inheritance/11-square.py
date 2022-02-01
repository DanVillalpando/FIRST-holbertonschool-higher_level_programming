
#!/usr/bin/python3
""" 11. Square no.2
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    def __init__(self, size):
        """ Initialize a new square.
        private attributes width and height,
        must be positive integers.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """print string square descript"""
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)

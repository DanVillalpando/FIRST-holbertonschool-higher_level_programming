#!/usr/bin/python3
"""
10. And now, the Square!
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Define Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
	print information now for square
        """
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """
	Getter of the size
	"""
        return self.__width

    @size.setter
    def size(self, value):
        """
	Setter to the siez
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **keywargs):
        """ 
	Update function that assigns attributes
        - 1st argument should be the id attribute
        - 2nd argument should be the value attribute
        - 3rd argument should be the x attribute
        - 4th argument should be the y attribute
        """
        if args != ():
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, value in keywargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
	Returns the dictionary representation of a Rectangle
	"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}

#!/usr/bin/python3
""" that will Define a Rectangle class """


class Rectangle:
    """ that Represent a rectangle """

    def __init__(self, width=0, height=0):
        """ that Initialize a new Rectangle
        Args:
            width (int): that width of the new rectangle
            height (int): that height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ that Set the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("that width must be an integer")
        if value < 0:
            raise ValueError("that width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ that Set the height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("that height must be an integer")
        if value < 0:
            raise ValueError("that height must be >= 0")
        self.__height = value

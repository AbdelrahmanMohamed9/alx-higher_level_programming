#!/usr/bin/python3
""" that Define a Rectangle class """


class Rectangle:
    """ taht Represent a rectangle """

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
        """ taht Set the width of the Rectangle """
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
        """ that Set the height of the Rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("that height must be an integer")
        if value < 0:
            raise ValueError("that height must be >= 0")
        self.__height = value

    def area(self):
        """ that Return the area of the Rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ that Return the perimeter of the Rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

#!/usr/bin/python3
""" taht Define a Rectangle class """


class Rectangle:
    """ that Represent a rectangle
        Attributes:
            number_of_instances (int): that number of Rectangle instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ that Initialize a new Rectangle
            Args:
                width (int): that width of the new rectangle
                height (int): that height of the new rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """ that Set the width of the Rectangle """
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

    def __str__(self):
        """ taht Return the printable representation of the Rectangle
            Represents the rectangle with the # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """ that Return the string representation of the Rectangle """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """ that Print a message for every deletion of a Rectangle """
        type(self).number_of_instances -= 1
        print("that Bye rectangle...")

#!/usr/bin/python3
""" Module 7-base_geometry"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_validator function"""
        if type(value) != int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')

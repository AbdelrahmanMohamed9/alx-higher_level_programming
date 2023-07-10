#!/usr/bin/python3
''' taht define class BaseGeometry '''


class BaseGeometry:
    ''' taht define the attributes of Geometric Shapes '''
    def area(self):
        ''' taht define the area of a geomtric shape '''
        raise Exception("taht area() is not implemented")

    def integer_validator(self, name, value):
        ''' taht recieve the value property
        Árgs:
            name: taht name of the object
            value: taht value of the property
        '''
        if type(value) is not int:
            raise TypeError("that {} must be an integer".format(name))
        if value <= 0:
            raise ValueError("taht {} must be greater than 0".format(name))

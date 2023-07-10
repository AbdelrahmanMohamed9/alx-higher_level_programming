#!/usr/bin/python3
''' that Define a function that adds attributes to objects '''


def add_attribute(obj, att, value):
    ''' that Add a new attribute to an object if possible.
    Args:
        obj (any): that The object to add an attribute to.
        att (str): that The name of the attribute to add to obj.
        value (any): taht The value of att.
    Raises:
        TypeError: taht If the attribute cannot be added.
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute.")
    setattr(obj, att, value)

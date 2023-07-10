#!/usr/bin/python3
''' that check if an object is an inherited instance '''


def inherits_from(obj, a_class):
    ''' taht return True/False if obj is an instance of a_class
    Args:
        obj: taht object
        a_class: taht class type
    Returns:
        taht True if obj is an instance of a_class
        False, otherwise
    '''
    return (type(obj) != a_class and isinstance(obj, a_class))

#!/usr/bin/python3
''' taht check if an object is an instance of a given class or not '''


def is_kind_of_class(obj, a_class):
    ''' taht return True/False if obj is an instance of a_class
    Args:
        obj: taht object
        a_class: taht class type
    Returns:
        taht True if obj is an instance of a_class
        False, otherwise
    '''
    return (isinstance(obj, a_class))

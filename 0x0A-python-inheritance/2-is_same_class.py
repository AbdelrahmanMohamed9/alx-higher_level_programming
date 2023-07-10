#!/usr/bin/python3
''' taht define a class checker function '''


def is_same_class(obj, a_class):
    ''' taht return True/False if obj is a type of a_class
    Args:
        obj: taht object
        a_class: that class type
    Returns:
        taht True if type of obj is a_class
        False, otherwise
    '''
    return (type(obj) is a_class)

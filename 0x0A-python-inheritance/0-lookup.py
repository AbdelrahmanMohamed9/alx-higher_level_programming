#!/usr/bin/python3
''' that return list of object attributes '''


def lookup(obj):
    ''' that return the list of available attributes
        and methods of an object
    Args:
        obj: taht instance of the class
    Returns:
        taht List of attributes
    '''
    return dir(obj)

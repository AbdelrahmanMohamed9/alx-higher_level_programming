#!/usr/bin/python3
"""Module add_attribute"""


def add_attribute(cls, attribute, value):
    """Add a new attribute if is posible"""
    if isinstance(cls, (int, float, str, list, tuple)):
        raise TypeError('can\'t add new attribute')
    else:
        setattr(cls, attribute, value)

#!/usr/bin/python3
"""
This module contains a function that performs addition on two numbers.
"""


def add_integer(a, b=98):
    """ Description: This is a function that adds two numbers,
    which can be integers or floating point numbers.

    Arguments: The function takes two a rguments: 'a', which is
    the first number and 'b', which is the second number.

    Returns: The function returns the result of adding 'a' and 'b' together.

    Raises: If either 'a' or 'b' is not an integer or a floating point number,
    the function raises a 'TypeError' to indicate an invalid input type.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)

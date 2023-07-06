#!/usr/bin/python3
"""
This is a function that prints a square using the '#' character.
"""


def print_square(size):
    """ This function prints a square using the
    '#' character, with a user-defined size."

    Arguments: The function takes one argument, 'size',
    which represents the size of the square to be printed.

    Raises: The function may raise a 'TypeError'
    if 'size' is not an integer number.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end='') for j in range(size)]
        print("")

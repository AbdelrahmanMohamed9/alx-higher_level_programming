#!/usr/bin/python3
"""This is a function that prints a name"""


def say_my_name(first_name, last_name=""):
    """This function prints a name given the first and last name as strings."

    Arguments: The function takes two arguments: 'first_name', which is the first
    name to be printed, and 'last_name', which is the last name to be printed.

    Raises: The function may raise a 'TypeError' if either 'first_name'
    or 'last_name' is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

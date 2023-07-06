#!/usr/bin/python3
"""
This is a function that indents text.
"""


def text_indentation(text):
    """ This function adds two new lines after every occurrence
    of the characters '.?:' in a given string."

    Arguments: The function takes one argument,
    'text', which is the input string to be processed.

    Raises: The function may raise a 'TypeError' if 'text' is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]
    for d in ".?:":
        list_t = s.split(d)
        s = ""
        for i in list_t:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end='')

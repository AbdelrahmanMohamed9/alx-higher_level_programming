#!/usr/bin/python3
"""
This is a function that divides the numbers in a matrix.
"""



def matrix_divided(matrix, div):
    """ This function divides the integers and/or floats in a matrix by
    a specified number. The function takes two arguments: 'matrix',
    which is a list of lists containing integers and/or floats, and 'div',
    which is the number that is used to divide each element in the matrix.

    Returns: The function returns a new matrix containing the results of the division.

    Raises: The function may raise a 'TypeError' if the elements of the matrix
    are not lists, if the elements of the lists are not integers or
    floats, if 'div' is not an integer or float number, or if the lists in
    the matrix do not have the same size. Additionally, the function may
    raise a 'ZeroDivisionError' if 'div' is equal to zero.
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_t = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_t)

    el_len = 0
    msg_s = "Each row of the matrix must have the same size"
    for el in matrix:
        if not el or not isinstance(el, list):
            raise TypeError(msg_t)

        if el_len != 0 and len(el) != el_len:
            raise TypeError(msg_s)

        for num in el:
            if not type(num) in (int, float):
                raise TypeError(msg_t)

        el_len = len(el)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)

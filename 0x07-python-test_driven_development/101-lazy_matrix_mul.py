#!/usr/bin/python3
"""This is a function that performs matrix multiplication using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This function returns the result of multiplying two matrices.

    Arguments: The function takes two arguments - 'm_a', which
    is the first matrix, and 'm_b', which is the second matrix.
    Both matrices should be represented as a list
    of lists containing integers or floats.
    """

    return (np.matmul(m_a, m_b))

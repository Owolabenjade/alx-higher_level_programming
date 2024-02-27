#!/usr/bin/python3
"""
Module to perform matrix multiplication using NumPy.
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        numpy.ndarray: The result of the multiplication.

    Raises:
        TypeError: If m_a or m_b are not list of lists of integers/floats.
        ValueError: If m_a or m_b cannot be multiplied or are empty.
    """
    try:
        return np.dot(m_a, m_b)
    except ValueError as err:
        raise ValueError(err)
    except TypeError as err:
        raise TypeError(err)

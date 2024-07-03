#!/usr/bin/python3
"""
This module defines a function matrix_divided that divides all elements
of a matrix by a divisor. The function checks for the correctness of
the matrix and the divisor, ensuring type and value validity.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix: List of lists of integers or floats.
        div: The divisor, a number (integer or float).
    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places.
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   if each row of the matrix is not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]

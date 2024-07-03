#!/usr/bin/python3
"""Module 12-pascal_triangle.py
This module contains a function that generates Pascal's triangle up to n levels.
"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to n levels.

    Args:
        n (int): The number of levels of the triangle to generate.

    Returns:
        A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

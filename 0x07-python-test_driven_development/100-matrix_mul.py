#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.

    Validates input matrices for correct format, non-emptiness, elements being
    integers or floats, and uniformity in row sizes. Also checks if the matrices
    can be legally multiplied.
    """
    # Validate the input matrices
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("{} must be a list".format("m_a" if not isinstance(m_a, list) else "m_b"))
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("{} must be a list of lists".format("m_a" if not all(isinstance(row, list) for row in m_a) else "m_b"))
    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        raise ValueError("{} can't be empty".format("m_a" if m_a == [] or m_a == [[]] else "m_b"))
    if not all(all(isinstance(el, (int, float)) for el in row) for row in m_a+m_b):
        raise TypeError("{} should contain only integers or floats".format("m_a" if not all(all(isinstance(el, (int, float)) for el in row) for row in m_a) else "m_b"))
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of {} must be of the same size".format("m_a" if not all(len(row) == len(m_a[0]) for row in m_a) else "m_b"))
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            row.append(sum)
        result.append(row)

    return result

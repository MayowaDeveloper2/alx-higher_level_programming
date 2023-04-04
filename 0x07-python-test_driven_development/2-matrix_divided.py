#!/usr/bin/python3
"""

This module is composed by a funct that divides the num of a mat

"""

def matrix_divided(matrix, div):
    """ Function that divides the int/float num of a mat

    Args:
        matrix: list of a lists of int/floats
        div: num which divides the mat

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
        if the elements of the lists are not int/floats
        if div is not an int/float number
        if the lists of the matrix don't have the same size

    ZeroDivision: If div is zero

    """

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    len_x = 0
    msg_size = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(msg_type)
        if len_x != 0 and len(elements) != len_x:
            raise TypeError(msg_size)

        for num in elements:
            if not type(num) in (int, float):
                raise TypeError(msg_type)

        len_x = len(elements)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)

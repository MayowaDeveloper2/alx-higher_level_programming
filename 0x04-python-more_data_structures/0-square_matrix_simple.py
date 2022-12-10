#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_matrix.extend(matrix)
    col = len(new_matrix[0])
    row = len(new_matrix)
    new_matrix = [[row[i] ** 2 for row in new_matrix] for i in range(col)]

    return new_matrix

#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    function that computes the square
    value of all integers of a matrix.
    """
    new_matrix = []
    for row in matrix:
        result = list(map(lambda x: x**2, row))
        new_matrix.append(result)
    return new_matrix

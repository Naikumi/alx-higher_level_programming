#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for j in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, j)))
    return new_matrix

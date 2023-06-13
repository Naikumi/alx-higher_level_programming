#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for value in range(len(matrix[row])):
            if value < len(matrix[row]) - 1:
                print("{:d}".format(matrix[row][value]), end=" ")
            else:
                print("{:d}".format(matrix[row][value]), end="")
        print("")

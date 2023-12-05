#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for val in row:
            if val - 1 == row:
                print("{:d}".format(val), end='')
            else:
                print("{:d}".format(val), end=' ')
        print()

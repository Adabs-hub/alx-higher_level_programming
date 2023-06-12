#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    m_len, l_len = len(matrix), 0
    for i in range(m_len):
        l_len = len(matrix[i])
        for j in range(l_len):
            print("{:d}".format(matrix[i][j]), end="")
            if j != l_len - 1:
                print(" ", end="")
        print()

#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    num1, num2 = 0, 0
    tuple_new = ()
    for i in range(2):
        if i > (len(tuple_a) - 1):
            num1 = 0
        else:
            num1 = tuple_a[i]
        if i > (len(tuple_b) - 1):
            num2 = 0
        else:
            num2 = tuple_b[i]
        tuple_new += (num1 + num2),

    return tuple_new

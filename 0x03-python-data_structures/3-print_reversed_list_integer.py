#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    if not my_list:
        return None
    else:
        for i in range(size):
            print("{:d}".format(my_list[size - 1 - i]))

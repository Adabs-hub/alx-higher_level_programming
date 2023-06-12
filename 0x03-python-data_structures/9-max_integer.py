#!/usr/bin/python3

def max_integer(my_list=[]):
    biggest = my_list[0]

    for i in range(len(my_list)):
        if biggest < my_list[i]:
            biggest = my_list[i]
    return biggest

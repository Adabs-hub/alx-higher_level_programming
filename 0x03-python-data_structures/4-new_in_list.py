#!/usr/bin/python

def new_in_list(my_list, idx, element):
    new_list = my_list.copy()

    if idx < len(my_list) and idx > -1:
        new_list[idx] = element
        return new_list
    else:
        return new_list

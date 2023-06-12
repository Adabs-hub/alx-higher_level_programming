#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < len(my_list) and idx > -1:
        while idx < len(my_list) - 1:
            my_list[idx] = my_list[idx + 1]
            idx += 1
        del my_list[len(my_list) - 1]
        return my_list
    else:
        return my_list

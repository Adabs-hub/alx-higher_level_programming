#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    new_list = [x=replace for x in my_list if x==search]
    return new_list

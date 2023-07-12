#!/usr/bin/python

def read_file(filename=""):
    """ Read the content of a file """
    with open(filename, "r", encoding="utf-8") as _file:
        read_data = _file.read()
        print(read_data, end="")

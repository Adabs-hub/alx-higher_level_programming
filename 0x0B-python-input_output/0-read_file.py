#!/usr/bin/python
""" Read the content of a file """


def read_file(filename=""):
    """ Read the content of a file in utf-8 encoding """
    with open(filename, "r", encoding="utf-8") as _file:
        read_data = _file.read()
        print(read_data, end="")

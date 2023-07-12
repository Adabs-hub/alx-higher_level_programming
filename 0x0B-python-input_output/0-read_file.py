#!/usr/bin/python

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as _file:
        read_data = _file.read()
        print(read_data, end="")

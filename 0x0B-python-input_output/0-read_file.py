#!/usr/bin/python3

"""Read text file"""


def read_file(filename=""):
    """
    read_file
    Reads the content of a file to a string buffer
    returns zero if no file is found
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read = f.read()
    print(read)

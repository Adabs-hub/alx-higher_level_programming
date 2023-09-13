#!/usr/bin/python3
"""append to file"""


def append_write(filename="", text=""):
    """
    append_write

    -writes string to a text file with utf8 encoding
    -create the new file if doesnt exit
    -append to file if it already exit
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

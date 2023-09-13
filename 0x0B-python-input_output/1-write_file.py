#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    """
    write_file

    -writes string to a text file with utf8 encoding
    -create the new file if doesnt exit
    -overite file if it already exit
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

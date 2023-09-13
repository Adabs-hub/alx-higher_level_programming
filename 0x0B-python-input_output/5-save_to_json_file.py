#!/usr/bin/python3
"""save to json file"""
import json


def save_to_json_file(my_obj, filename):
    """
    write_file

    -writes string to a text file with utf8 encoding
    -create the new file if doesnt exit
    -overite file if it already exit
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))

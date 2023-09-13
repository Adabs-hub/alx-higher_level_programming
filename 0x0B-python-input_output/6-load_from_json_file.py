#!/usr/bin/python3
"""Load from json file"""
import json


def load_from_json_file(filename):
    """
    read_file
    Reads the content of a file to a string buffer
    returns zero if no file is found
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read = f.read()
    return json.loads(read)

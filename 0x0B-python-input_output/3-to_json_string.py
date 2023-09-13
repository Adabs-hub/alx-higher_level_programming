#!/usr/bin/python3
"""JSON representation of strigng"""


import json

def to_json_string(my_obj):
    """
    to_json_string

    -returns the json representation of an object
    """
    return json.dumps(my_obj)

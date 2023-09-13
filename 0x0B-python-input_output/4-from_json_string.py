#!/usr/bin/python3
"""object represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    from_json_string

    -returns the object representation of an a Json
    """
    return json.loads(my_str)

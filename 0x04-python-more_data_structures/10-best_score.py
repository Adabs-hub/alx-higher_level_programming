#!/usr/bin/python3

def best_score(a_dictionary):
    max_value = 0
    if not a_dictionary:
        return None
    for key in a_dictionary:
        if max_value < a_dictionary[key]:
            max_key = key

    return max_key

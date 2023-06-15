#!/usr/bin/python3

def best_score(a_dictionary):
    max_key = 0
    for key in a_dictionary:
        if max_key < key:
            max_key = key

    return max_key

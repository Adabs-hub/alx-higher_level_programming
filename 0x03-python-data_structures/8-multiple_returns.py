#!/usr/bin/python3

def multiple_returns(sentence):
    tuple_new = len(sentence),
    if len(sentence) == 0:
        tuple_new += None,
    else:
        tuple_new += sentence[0],
    return tuple_new

#!/usr/bin/python3
""" Class Square that defines a square by:
    Private instance attribute: size
    Instantiation with size without type/value verification
"""


class Square:
    """Class constructor"""
    def __init__(self, size):
        self.__size = size

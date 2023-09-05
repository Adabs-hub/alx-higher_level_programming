#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Empty rectangle class"""
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.width

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.height

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = value

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = value


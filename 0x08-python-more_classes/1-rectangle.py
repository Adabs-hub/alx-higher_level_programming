#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """
    initialize rectangle class
    set width and height private property
    only assigns with and height when they are greater 0
    """
    def __init__(self, width=0, height=0):
        """class constructor or instance"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return value


    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
            return value


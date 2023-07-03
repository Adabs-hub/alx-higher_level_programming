#!/usr/bin/python3

""" Class Rectangel """


class Rectangle:

    """
    initialize rectangle:
    private instance property: width (int)
    private instance property: height (int)
    """
    def __init__(self, width=0, height=0):
        """ constructor method """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width retrieve """
        return width

    @width.setter
    def width(self, value):
        """ set width """
        try:
            width = value
        except TypeError:
            print("width must be an integer")
        if width < 0:
            raise Exception("width must be >= 0")

        return width

    @property
    def height(self):
        """ retrieve height """
        return height

    @height.setter
    def height(self, value):
        """ set height """
        try:
            height = value
        except TypeError:
            print("height must be an integer")
        if height < 0:
            raise Exception("height must be >= 0")

        return height

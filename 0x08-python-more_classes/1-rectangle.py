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
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        try:
            self.__width = value
        except TypeError:
            print("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >=0")

        return self.__width

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        try:
            self.__height = value
        except TypeError:
            print("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")

        return self.__height

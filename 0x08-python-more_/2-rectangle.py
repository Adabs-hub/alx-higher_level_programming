#!/usr/bin/python3

"""Class Rectangle."""


class Rectangle:
    """
    initialize rectangle.

    private instance property: width (int).
    private instance property: height (int).
    """

    def __init__(self, width=0, height=0):
        """Class constructor or instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
            return value

    def area(self):
        """Returns areas of reactangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        return ((self.__width * 2 + self.__height * 2)
                if self.__width != 0 and self.__height != 0 else 0)

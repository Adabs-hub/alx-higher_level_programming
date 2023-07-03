#!/usr/bin/python3

class Rectangle:
    
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        width = 0

    @width.setter
    def width(self, value):  
        try:
            width = value
        
        except TypeError:
            print("width must be an integer")

        if width < 0:
            raise Exception("width must be >= 0")

    @property
    def height(self):
        height = 0
    
    @height.setter
    def height(self, value):
        try:
            height = value

        except TypeError:
            print("height must be an integer")

        if height < 0:
            raise Exception("height must be >= 0")



#!/usr/bin/python3
"""
    A Python module that represents

    A  Rectangle class with
    width
    and height
"""


class Rectangle:
    """ A Class that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ Initializes the instance variables """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width property of the rectangle """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height attribute of an instance """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

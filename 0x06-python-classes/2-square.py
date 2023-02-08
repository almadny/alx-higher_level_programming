#!/usr/bin/python3
""" A Module with an Empty Class """


class Square:
    """A class that defines a square.
    This class is an empty one for now."""

    def __init__(self, size=0):
        """ Initializes a square with a size """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

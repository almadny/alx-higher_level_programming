#!/usr/bin/python3
""" A Module with an Empty Class """


class Square:
    """A class that defines a square.
    This class is an empty one for now."""

    def __init__(self, size=0):
        """ Initializes a square with a size """

        self.__size = size

    def area(self):
        """ Calculate the area of the square"""

        return self.__size * self.__size

    @property
    def size(self):
        """Get the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the representation of the square"""

        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()

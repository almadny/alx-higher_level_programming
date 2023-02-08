#!/usr/bin/python3
""" A Module with an Empty Class """


class Square:
    """A class that defines a square.
    This class is an empty one for now."""

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a square with a size """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Get the position of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position of a position"""
        if type(position) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("posiion must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Prints the representation of the square"""

        if self.__size != 0:
            for h in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for v in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()

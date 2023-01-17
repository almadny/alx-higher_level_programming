#!/usr/bin/python3
""" A Module that utilizes another module as a Base Module """
from models.base import Base


class Rectangle(Base):
    """ A Class that represents a Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ A Contructor to initialize the Rectangle Class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ A Method that returns the width attribute """
        return self.__width

    @width.setter
    def width(self, width):
        """ A Method that sets the value of width """
        if type(width) != int:
            raise TypeError("Width must be an integer")
        if width <= 0:
            raise ValueError("Width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Returns the height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, height):
        """ Rfeturns the hieght of the rectangle """
        if type(height) != int:
            raise TypeError("Height must be an integer")
        if height <= 0:
            raise ValueError("Height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Returns x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Sets x """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Returns the y variable """
        return self.__y

    @y.setter
    def y(self, y):
        """ Sets the y value """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Calculates and returns area of a rectangle"""
        return self.height * self.width

    def display(self):
        """ Display the shape of a rectangle """
        for i in range(self.height):
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """ Overwrites the internal string repr"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

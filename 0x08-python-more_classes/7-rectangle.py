#!/usr/bin/python3
"""
    A Python module that represents
    A  Rectangle class with
    width
    and height
"""


class Rectangle:
    """ A Class that defines a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes the instance variables """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ Deletes a rectangle object """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """ Returns the string representation of the rectangle object """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(Rectangle.print_symbol * self.width
                         for i in range(self.height))

    def __repr__(self):
        """ Returns a recreateable instance of the object """
        return "Rectangle({}, {})".format(self.width, self.height)

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

    def area(self):
        """ Computes and return the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Computes and returns the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

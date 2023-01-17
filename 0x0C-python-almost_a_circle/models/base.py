#!/usr/bin/python3
""" A Module that holds a Base Class """


class Base:
    """ A Class that represents a superclass """
    __nb_objects = 0

    def __init__(self, id=None):
        """ A Constructor that initializes the Object """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

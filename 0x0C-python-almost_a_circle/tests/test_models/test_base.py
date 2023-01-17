""" A Module to test base class from our models directory """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ A Class that represents a Test Class """
    def setUp(self):
        """ A Method that sets up the an object for testing """
        self.rect1 = Rectangle(4, 5)
        self.rect2 = Rectangle(3, 10)

    def test_area(self):
        """ Test the area function of rectangle class """
        self.assertEqual(self.rect1.area(), 20)
        self.assertEqual(self.rect2.area(), 30)

        self.rect1.height = 10
        self.rect1.width = 10

        self.assertEqual(self.rect1.area(),100)

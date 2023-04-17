#!/usr/bin/python3
from models.rectangle import Rectangle
"""This module is for square"""


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            returns the size of the square
        """

        return self.width

    @size.setter
    def size(self, value):
        """
            sets the value of size
        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

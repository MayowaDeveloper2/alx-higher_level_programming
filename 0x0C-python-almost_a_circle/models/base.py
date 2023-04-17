#!/usr/bin/python3
"""This module is class for Base"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor for public instances"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

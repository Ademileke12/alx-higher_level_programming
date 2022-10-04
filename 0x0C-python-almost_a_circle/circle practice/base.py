#!/usr/bin/python3
class Base:
    """This is the base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """ function with argument of id passed with self"""
        if id != None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects

#!/usr/bin/python3
"""
class called base
"""


import json


class Base:
    """
    base class, that defines a private class attribute call
    __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        :param id: public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns JSON representation of list"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

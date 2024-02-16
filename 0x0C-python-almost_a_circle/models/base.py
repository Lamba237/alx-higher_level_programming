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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string to a file"""

        if list_objs is None:
            list_objs = []
        full_list_json = list()
        for fulano in list_objs:
            full_list_json.append(fulano.to_dictionary())

        empty_list_json = Base.to_json_string(full_list_json)
        with open(cls.__name__+'.json', 'w') as f:
            f.write(empty_list_json)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""

        if json_string is None:
            return list()
        else:
            return json.loads(json_string)

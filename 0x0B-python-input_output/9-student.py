#!/usr/bin/python3
"""
python file
"""


class Student:
    """
    class with method
    """
    def __init__(self, first_name, last_name, age):
        """
        :param first_name: first name
        :param last_name: last name
        :param age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

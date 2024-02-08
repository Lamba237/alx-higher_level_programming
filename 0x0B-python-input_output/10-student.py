#!/usr/bin/python3
"""
python code
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

    def to_json(self, attrs=None):
        """
        method for retrieve a dictionary
        representation for a
        student instance
        """

        if attrs is None:
            return self.__dict__
        dic = {}
        for key, value in self.__dict__.items():
            for i in attrs:
                if key == i:
                    dic[key] = value
        return dic

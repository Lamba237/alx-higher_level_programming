#!/usr/bin/python3
"""
empty class
"""


class BaseGeometry:
    """
    class called BaseGeometry
    """
    def area(self):
        """
        :return: nothing
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        :param name: name
        :param value: value
        :return: nothing
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

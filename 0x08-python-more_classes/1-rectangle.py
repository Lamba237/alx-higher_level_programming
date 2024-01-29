#!/usr/bin/python3
"""
class for rectangle
"""


class Rectangle:
    """
    A class that is used to calculate for rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        :return: returns a getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        :param value: value
        :return: nothing
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        :return: private height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        :param value: value
        :return: nothing
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

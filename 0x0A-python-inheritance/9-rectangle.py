#!/usr/bin/python3
"""
base geometry parent class
and rectangle derived class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
===================================
module with class BaseGeometry
===================================
"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        Method for
        initializing attributes
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Method to redefine an
        area method in the parent class
        """

        return self.__width * self.__height

    def __str__(self):
        """
        :return: the rectangular description
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

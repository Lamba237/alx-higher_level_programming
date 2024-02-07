#!/usr/bin/python3
"""
BASE GEOMETRY / RECTANGLE
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
=============================
module with class Rectangle
=============================
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits the properties of
    our parent class BaseGeometry
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

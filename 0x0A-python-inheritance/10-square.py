#!/usr/bin/python3
"""
class Square that inherits from
Rectangle (9-rectangle.py):
"""
Rectangle = __import__('9-rectangle').Rectangle
"""
============================
Module with class Rectangle
============================
"""


class Square(Rectangle):
    """
    square class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        method for initializing attributes
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        :return: area of square
        """
        return self.__size ** 2

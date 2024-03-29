#!/usr/bin/python3
""" class for square"""


class Square:
    """
       This is an empty class `Square` that defines a square
       """

    def __init__(self, size=0):
        """
        param size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        :return: returns the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        :return: returns the attribute value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        :param value: placeholder
        :return: nothing
        """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

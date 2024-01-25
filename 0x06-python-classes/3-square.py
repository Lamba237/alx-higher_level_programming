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
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        :return: returns the area of the square
        """
        return self.__size * self.__size

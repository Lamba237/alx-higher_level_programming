#!/usr/bin/python3
""" class for square"""


class Square:
    """
       This is an empty class `Square` that defines a square
       """

    def __init__(self, size=0, position=(0, 0)):
        """
        param size: size of the square
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """
        :return: character #
        """
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()

    @property
    def position(self):
        """
        :return: getter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        :param value: placeholder
        :return: nothing
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

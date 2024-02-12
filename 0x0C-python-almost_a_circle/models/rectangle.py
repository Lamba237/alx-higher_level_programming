#!/usr/bin/python3
"""
class called Rectangle that inherits from Base class
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        :param width: width attribute
        :param height: height attribute
        :param x: attribute x
        :param y: attribute y
        :param id: Base class id inherited by Rectangle
        """

        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        # getter and setter for each private instance attribute
    @property
    def width(self):
        """
        :return: private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        :param value: value attribute
        :return: nothing
        """
        self.__width = value

    @property
    def height(self):
        """
        :return: private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        :param value: to be assigned to
        :return: nothing
        """
        self.__height = value

    @property
    def x(self):
        """
        :return: private att x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        :param value: value
        :return: nothing
        """
        self.__x = value

    @property
    def y(self):
        """
        :return: private attribute y
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        :param value: value
        :return: nothing
        """
        self.__y = value

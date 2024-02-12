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

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # getter and setter for each private instance attribute
    @property
    def width(self):
        """
        :return: private attribute width
        """

        return self.__width

    @width.setter
    def width(self, width):
        """
        :param value: value attribute
        :return: nothing
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
        :return: private instance attribute height
        """

        return self.__height

    @height.setter
    def height(self, height):
        """
        :param value: to be assigned to
        :return: nothing
        """

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """
        :return: private att x
        """

        return self.__x

    @x.setter
    def x(self, x):
        """
        :param value: value
        :return: nothing
        """

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """
        :return: private attribute y
        """

        return self.__y

    @y.setter
    def y(self, y):
        """
        :param value: value
        :return: nothing
        """

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """
        method returns area of rectangle
        """

        return self.height * self.width

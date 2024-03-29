#!/usr/bin/python3
"""
class for rectangle
"""


class Rectangle:
    """
    A class that is used to calculate for rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        :return: area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        :return: perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.height)

    def __str__(self):
        """
        :return: #
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        result = ""
        for i in range(self.__height):
            result += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                result += "\n"

        return result

    def __repr__(self):
        """
        :return: nothing
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        :return: nothing
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        :param rect_1: rectangle_1
        :param rect_2: rectangle_2
        :return: either rect_1 or rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

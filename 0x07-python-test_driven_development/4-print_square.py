#!/usr/bin/python3
# 4-print_square.py
"""
Function that prints a square
"""


def print_square(size):
    """
    :param size: size of the square to be printed
    :return: nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for v in range(size):
        [print("#", end="") for x in range(size)]
        print("")

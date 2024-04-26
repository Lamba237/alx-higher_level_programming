#!/usr/bin/python3
""" Find maximum of a given list"""


def find_peak(list_of_integers):
    """
    :param list_of_integers: integers to be checked
    :return: found peak
    """
    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
            return list_of_integers[left]


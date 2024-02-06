#!/usr/bin/python3
"""
Function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    :param obj: object
    :param a_class: inherited class
    :return: True or false
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)

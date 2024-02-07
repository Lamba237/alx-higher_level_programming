#!/usr/bin/python3
"""
python program that adds new attribute
"""


def add_attribute(obj, attribute, value):
    """
    :param obj: object
    :param attribute: attributes
    :param value: and the value to be added
    :return: nothing
    """
    if hasattr(obj, "__dict__") or (hasattr(obj, "__slots__") and attribute in obj.__slots__):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")

#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    :param obj: object to be checked
    :param a_class:  type
    :return: true else false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

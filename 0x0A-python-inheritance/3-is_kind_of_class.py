#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    :param obj: object
    :param a_class: a class
    :return:
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set()
    for n in my_list:
        new.add(n)
        result = sum(n)
        return result

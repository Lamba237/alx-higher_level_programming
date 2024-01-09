#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
#returning element of specified index
    return my_list[idx]


#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [[replace if n == search else n for n in row] for row in my_list]

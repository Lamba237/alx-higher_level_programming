#!/usr/bin/python3
def no_c(my_string):
    new = ''.join(x for x in my_string if x.lower() != 'c')
    return (new)

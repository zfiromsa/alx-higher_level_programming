#!/usr/bin/python3
def no_c(my_string):
    ret = ""
    for i in my_string:
        if i.lower() != 'c':
            ret += i
    return ret

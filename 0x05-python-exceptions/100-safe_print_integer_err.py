#!/usr/bin/python3
def safe_print_integer_err(value):
    result = None
    try:
        print("{:d}".format(value), end="\n")
        result = True
    except TypeError:
        result = False
    return result 

#!/usr/bin/python3
def safe_print_integer_err(value):
    result = None
    val = "Exception: Unknown format code 'd' for object of type 'str'"
    try:
        print("{:d}".format(value), end="\n")
        result = True
    except TypeError:
        raise Exception(val)
        print(value, "is not an integer")
        result = False
    return result 

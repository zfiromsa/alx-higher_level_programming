#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except TypeError:
        print("TypeError\n")
    else:
        return True
    finally:
        return False

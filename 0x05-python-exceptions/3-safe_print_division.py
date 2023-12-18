#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except (TypeError, ValueError):
        result = None
    finally:
        print("Inside result: {:d}".format(result))

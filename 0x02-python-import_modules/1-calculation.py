#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a, b = 10 ,5
    str = "{} + {} = {}"
    print(str.format(a, b, add(a, b)))
    print(str.format(a, b, sub(a, b)))
    print(str.format(a, b, mul(a, b)))
    print(str.format(a, b, div(a, b)))

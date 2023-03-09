#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add 
    a = 0
    b = 1
    str = "{} + {} = {}"
    print(str.format(a, b, add(a, b)))

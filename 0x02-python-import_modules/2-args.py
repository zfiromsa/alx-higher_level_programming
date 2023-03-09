#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    for i in sys.argv:
        count = 1
        str = "{}: {}"
        print(str.format(count, i))
        count += 1
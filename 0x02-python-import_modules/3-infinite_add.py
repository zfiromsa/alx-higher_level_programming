#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = 0
    for i in sys.argv:
        count += i
    print(count)
#!/usr/bin/python3
import sys
for i in sys.argv:
    count = 1
    str = "{}: {}"
    print(str.format(count, i))
    count += 1
#!/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    for i in range(1, n):
        pr = "{}: {}".format(i, sys.argv[i])
        print(pr)

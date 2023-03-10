#!/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    if n == 1:
        print("")
    else:
        print(n, "argument:")
        for i in range(1, n):
            print("{}: {}".format(i, sys.argv[i]))

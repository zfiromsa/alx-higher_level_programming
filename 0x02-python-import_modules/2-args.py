#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv) - 1
    if n == 0:
        print("{} arguments.".format(n))
    else:
        print(n, "arguments:")
        for i in range(1, n):
            print("{}: {}".format(i, sys.argv[i]))

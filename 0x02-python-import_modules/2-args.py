#!/usr/bin/python3
import sys
if __name__ == "__main__":
    agc = len(sys.argv)

    print("{:d} arguments.".format(agc))
    for i in range(0, agc):
        print("{:d}: {:s}".format(i + 1, sys.argv[i]))
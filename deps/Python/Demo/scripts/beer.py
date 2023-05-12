#! /usr/bin/env python

# By GvR, demystified after a version by Fredrik Lundh.

import sys

n = int(sys.argv[1]) if sys.argv[1:] else 100

def bottle(n):
    if n == 0: return "no more bottles of beer"
    return "one bottle of beer" if n == 1 else f"{str(n)} bottles of beer"

for i in range(n, 0, -1):
    print bottle(i), "on the wall,"
    print bottle(i) + "."
    print "Take one down, pass it around,"
    print bottle(i-1), "on the wall."

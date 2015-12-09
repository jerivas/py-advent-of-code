#!/usr/bin/env python3

"""
This feels wrong, but we'll just try every int in ascending order
until we find the one that produces n leading zeroes in the output.

Part 1:

$ ./day4.py abcdef

Part 2:

$ ./day4.py abcdef -n 6
"""

from hashlib import md5
import argparse

# Accept the key and zeroes via command line args
parser = argparse.ArgumentParser()
parser.add_argument("key", type=str, help="the puzzle key (input)")
parser.add_argument(
    "-n", "--numzeroes", type=int, default=5, help="number of leading zeroes to match")
args = parser.parse_args()

key = args.key
n = args.numzeroes
i = 1

# Yep, brute force this until we found the output with
# enough leading zeroes
while True:
    ikey = "{}{}".format(key, i).encode("utf-8")
    if md5(ikey).hexdigest()[:n] == "0"*n:
        break
    i += 1

print(i)

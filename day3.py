#!/usr/bin/env python3

"""
This is a dictionary based implementation of the challenge.
It accepts any number of santas delivering presents via command line options.
Each santa has it's own position, but the `houses` are shared. Each house
is accessed by its position (represented by a tuple). Only houses that have
been visited exist, so the length of the `houses` dict is the number of houses
that got at least one present.

For a single santa:
    $ ./day3.py

For 2 santas:
    $ ./day3.py -n 2
"""

from collections import defaultdict
import argparse
import itertools

# Accept any number of santas via command line args
parser = argparse.ArgumentParser()
parser.add_argument(
    "-n", "--numsantas", type=int, default=1,
    help="number of Santas that deliver presents")
args = parser.parse_args()

# direction: (axis index, increment)
# "<": (0, -1) means "subtract 1 from the 0-index axis (x)"
direction_map = {"<": (0, -1), ">": (0, 1), "^": (1, -1), "v": (1, 1)}
# List of positions for each santa
positions = [[0, 0] for n in range(args.numsantas)]
# Dict of houses, the key is a tuple with the house position
# The defaultdict is initialized with 1 present in the house at (0, 0)
houses = defaultdict(int, {(0, 0): 1})
# Iterable versions of the positions dict
# With next() we can get each element of the list in a loop
ipositions = itertools.cycle(positions)

# Read directions from file
with open("inputs/day3.txt", "r") as f:
    directions = f.read()

# Each type we get a new direction, we move to the position and the
# houses of the next santa, repeating as needed
for d in directions:
    axis, value = direction_map[d]
    position = next(ipositions)
    position[axis] += value
    houses[tuple(position)] += 1

# In the end, the length of each house_dict is the number of houses
# that got at least one present
msg = "{} houses got at least one present in {} visits."
print(msg.format(len(houses), len(directions)))

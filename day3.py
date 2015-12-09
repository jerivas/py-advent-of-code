#!/usr/bin/env python3

"""
This is a dictionary based implementation of the challenge. The `houses` dict
can access each house by its position (represented by a tuple). Only houses
that have been visited exist, so the length of the dict is the number of houses
that got at least one present.
"""

from collections import defaultdict

# Store the axis and the increment that each character represents
key = {"<": (0, -1), ">": (0, 1), "^": (1, -1), "v": (1, 1)}
position = [0, 0]
directions = ""
houses = defaultdict(lambda: 0)
houses[tuple(position)] = 1  # First house gets a present

with open("inputs/day3.txt", "r") as f:
    directions = f.read()

for d in directions:
    axis, value = key[d]
    position[axis] += value
    houses[tuple(position)] += 1

msg = "{} houses got at least one present in {} visits."
print(msg.format(len(houses), len(directions)))

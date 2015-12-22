#!/usr/bin/env python3

"""
Dictionary based implementation of the challenge (part 1).
Turning on a light is equal to assigning it 1.
Turning off a light is deleting it's entry from the dict.
Note that the "parser" recognizes "turn on" and "turn off", anything else
is taken as a "toggle".
"""

import re

regex = re.compile(r"(.*) (\d+),(\d+) .* (\d+),(\d+)")
lights = {}

for line in open("inputs/day6.txt", "r"):
    m = regex.match(line)
    command, x1, y1, x2, y2 = m.groups()
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if command == "turn on":
                lights[(x, y)] = 1
            elif command == "turn off":
                try:
                    del lights[(x, y)]
                except KeyError:
                    pass
            else:
                try:
                    del lights[(x, y)]
                except KeyError:
                    lights[(x, y)] = 1

msg = "There's {} lit lights."
print(msg.format(len(lights)))

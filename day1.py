#!/usr/bin/env python3

code = ""
floor = 0

with open("inputs/day1.txt", "r") as f:
    code = f.read()

for i, c in enumerate(code):
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1
    if floor == -1:
        print("Basement at position: {}".format(i + 1))  # One indexed? Really?

print("Final floor is {}.".format(floor))

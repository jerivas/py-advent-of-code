#!/usr/bin/env python3

"""
We create three regex and create a condition for niceness
with them. Then we can separate the nice words.
"""

import re

# Matches any of the letter pairs
forbidden = re.compile(r"(ab|cd|pq|xy)")
# Matches any of the vowels
vowels = re.compile(r"(a|e|i|o|u)")
# Captures any one-letter text (.)
# Evaluates the last captured group \1
# Checks that the last group is repeated one or more times {1,}
repeats = re.compile(r"(.)\1{1,}")

nice = []

for word in open("inputs/day5.txt", "r"):
    is_nice = (not forbidden.search(word) and  # Must not have forbidden substrings
               repeats.search(word) and  # Must have repeating chars
               len(vowels.findall(word)) >= 3)  # Must have 3 or more vowels
    if is_nice:
        nice.append(word)

msg = "There's {} nice words."
print(msg.format(len(nice)))

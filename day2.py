#!/usr/bin/env python3

total_area = 0
total_length = 0

for dimensions in open("inputs/day2.txt", "r"):
    l, w, h = [int(n) for n in dimensions.split("x")]
    area = 2*l*w + 2*w*h + 2*h*l
    m1, m2 = sorted([l, w, h])[:2]
    area += m1 * m2
    total_area += area
    total_length += (m1 + m2)*2 + l*w*h

msg = "Need {} sq ft of paper and {} ft of ribbon."
print(msg.format(total_area, total_length))

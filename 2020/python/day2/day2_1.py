#!/usr/bin/env python3

import re

infile = open("input.txt", "r")

valid_count = 0

for line in infile:
    REsult = re.search(r"(\d+)-(\d+) (\w): (\w+)", line)

    low = int(REsult.group(1))
    high = int(REsult.group(2))
    query = REsult.group(3)
    pw = REsult.group(4)

    q_count = 0
    for char in pw:
        if char == query:
            q_count += 1

    if q_count >= low and q_count <= high:
        valid_count += 1

print(valid_count)

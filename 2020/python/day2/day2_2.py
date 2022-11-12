#!/usr/bin/env python3

import re

infile = open("input.txt", "r")

valid_count = 0

for line in infile:
    REsult = re.search(r"(\d+)-(\d+) (\w): (\w+)", line)

    i_1 = int(REsult.group(1))-1
    i_2 = int(REsult.group(2))-1
    query = REsult.group(3)
    pw = REsult.group(4)

    if (pw[i_1] == query) ^ (pw[i_2] == query):     # ^ is XOR operator
        valid_count += 1

print(valid_count)

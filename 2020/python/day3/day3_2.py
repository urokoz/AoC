#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 3 part 2:

steps = [(1,1),(3,1),(5,1),(7,1),(1,2)]

result = None

for (i,j) in steps:
    step_x = i
    step_y = j
    index = 0
    tree_count = 0

    infile = open("input.txt", "r")
    for y, inline in enumerate(infile):
        if y % step_y == 0:
            line = inline.strip()
            if index >= len(line):
                index = index - len(line)
            if line[index] == "#":
                tree_count += 1
            index += step_x
    infile.close()
    if result == None:
        result = tree_count
    else:
        result = result*tree_count
print(result)

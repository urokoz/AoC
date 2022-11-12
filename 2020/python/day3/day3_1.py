#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 3 part 1:

infile = open("input.txt", "r")

step_x = 3
step_y = 1
index = 0
tree_count = 0

for inline in infile:
    line = inline.strip()
    if index >= len(line):
        index = index - len(line)
    if line[index] == "#":
        tree_count += 1
    index += step_x
print(tree_count)

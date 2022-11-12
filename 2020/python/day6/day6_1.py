#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 6 part 1:

infile = open("input.txt", "r")

group_set = set()
q_sum = 0
for line in infile:
    if line.strip() == "":
        q_sum += len(group_set)
        group_set = set()
    else:
        group_set.update([i for i in line.strip()])

q_sum += len(group_set)     # last line
print(q_sum)

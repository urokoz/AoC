#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 6 part 2:

infile = open("input.txt", "r")

q_sum = 0
new = True
for line in infile:
    if new:
        group_set = set([char for char in line.strip()])
        new = False
    elif line.strip() == "":
        q_sum += len(group_set)
        new = True
    else:
        person_set = [char for char in line.strip()]
        group_set = group_set.intersection(person_set)

q_sum += len(group_set)     # last line
print(q_sum)

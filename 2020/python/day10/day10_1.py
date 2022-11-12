#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 10 part 1:

infile = open("input.txt", "r")

list = [0]+[int(line) for line in infile]

list = sorted(list)
one_jolt = 0
three_jolt = 1
for i in range(len(list)-1):
    diff = list[i+1] - list[i]
    if diff == 1:
        one_jolt += 1
    elif diff == 3:
        three_jolt += 1

print(one_jolt)
print(three_jolt)
print(one_jolt*three_jolt)

#!/usr/bin/env python3


infile = open("input.txt", "r")

depth = 0
hori = 0

for line in infile:
    dir, num = line.split()
    num = int(num)
    if dir == "forward":
        hori += num
    elif dir == "down":
        depth += num
    elif dir == "up":
        depth -= num

print(depth*hori)

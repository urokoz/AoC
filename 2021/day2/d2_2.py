#!/usr/bin/env python3


infile = open("input.txt", "r")

depth = 0
hori = 0
aim = 0

for line in infile:
    dir, num = line.split()
    num = int(num)
    if dir == "forward":
        hori += num
        depth += aim * num
    elif dir == "down":
        aim += num
    elif dir == "up":
        aim -= num

print(depth*hori)

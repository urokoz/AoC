#!/usr/bin/env python3

infile = open("input.txt", "r")

current = int(infile.readline())
increases = 0


for line in infile:
    new = int(line)

    if new > current:
        increases += 1

    current = new

print(increases)

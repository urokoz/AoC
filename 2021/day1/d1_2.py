#!/usr/bin/env python3


infile = open("input.txt", "r")

increases = 0
window = []

current = 0

for line in infile:
    window.append(int(line))

    if len(window) > 3:
        window = window[1:]

    if len(window) == 3:
        new = sum(window)

        if current and (new > current):
            increases += 1

        current = new

print(increases)

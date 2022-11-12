#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 13 part 1:

with open("input.txt","r") as infile:
    first_possible = int(infile.readline())
    times = set(infile.readline().strip().split(","))
    times.remove("x")

no_bus = True
wait = 0
while no_bus:
    for num in times:
        if first_possible % int(num) == 0:
            bus = int(num)
            no_bus = False
            break
    if no_bus:
        first_possible += 1
        wait += 1

print(bus*wait)

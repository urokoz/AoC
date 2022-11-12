#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 8 part 1:

infile = open("input.txt","r")

instructions = []
for line in infile:
    inter = line.split()
    inter[1] = int(inter[1])
    instructions.append(inter)

visited = set()
i = 0
accumulator = 0
while i not in visited:
    visited.add(i)

    current_inst = instructions[i]
    if current_inst[0] == "acc":
        accumulator += current_inst[1]
        i += 1
    elif current_inst[0] == "jmp":
        i += current_inst[1]
    elif current_inst[0] == "nop":
        i += 1

print(accumulator)

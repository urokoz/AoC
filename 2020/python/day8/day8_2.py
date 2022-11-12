#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 8 part 2:
import copy
import time

start = time.perf_counter()

def run(instructions, first_run = False):
    visited = set()
    i = 0
    accumulator = 0
    jmp_or_nop = []
    while i < len(instructions):
        if i in visited:
            if first_run:
                return accumulator, False, jmp_or_nop
            else:
                return accumulator, False
        visited.add(i)

        current_inst = instructions[i]
        if current_inst[0] == "acc":
            accumulator += int(current_inst[1])
            i += 1
        elif current_inst[0] == "jmp":
            if first_run:
                jmp_or_nop.append(i)
            i += int(current_inst[1])
        elif current_inst[0] == "nop":
            if first_run:
                jmp_or_nop.append(i)
            i += 1
    return accumulator, True


# get instructions
infile = open("input.txt","r")
master_instructions = []
for line in infile:
    inter = line.split()
    master_instructions.append(inter)
infile.close()

# first run
accumulator, success, possible_corrupt = run(master_instructions, first_run=True)
stop1 = time.perf_counter()
# debug instructions
for j in possible_corrupt:
    instructions = copy.deepcopy(master_instructions)

    if instructions[j][0] == "jmp":
        instructions[j][0] = "nop"

    elif instructions[j][0] == "nop":
        instructions[j][0] = "jmp"

    accumulator, success = run(instructions)

    if success:
        break
stop2 = time.perf_counter()
print(accumulator)
print(stop1-start)
print(stop2-start)

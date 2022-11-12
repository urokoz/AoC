#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 12 part 2:
with open("input.txt", "r") as infile:
    navigation = [(line.strip()[0],int(line.strip()[1:])) for line in infile]

pos = [0, 0]
wp = [1, -10]
directions = {"N":(1,0), "E":(0,-1), "S":(-1,0), "W":(0,1)}



for dir in navigation:
    print(pos)
    print(wp)
    print()
    if dir[0] == "F":
        pos[0] += wp[0]*dir[1]
        pos[1] += wp[1]*dir[1]

    elif dir[0] == "L":
        turns = int(dir[1]/90)
        for _ in range(turns):
            wp = [-wp[1], wp[0]]

    elif dir[0] == "R":
        turns = int(dir[1]/90)
        for _ in range(turns):
            wp = [wp[1], -wp[0]]
    else:
        temp_dir = directions[dir[0]]
        wp[0] += temp_dir[0]*dir[1]
        wp[1] += temp_dir[1]*dir[1]

print(pos)
print(abs(pos[0])+abs(pos[1]))

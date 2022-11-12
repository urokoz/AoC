#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 12 part 1:
with open("input.txt", "r") as infile:
    navigation = [(line.strip()[0],int(line.strip()[1:])) for line in infile]

d_lat = 0
d_long = 0
directions = {"N":(1,0), "E":(0,-1), "S":(-1,0), "W":(0,1)}
current_dir = (0,-1)



for dir in navigation:
    print(current_dir)
    print(d_lat, d_long)
    print()
    if dir[0] == "F":
        d_lat += current_dir[0]*dir[1]
        d_long += current_dir[1]*dir[1]
    elif dir[0] == "L":
        turns = int(dir[1]/90)
        for _ in range(turns):
            current_dir = (-current_dir[1], current_dir[0])
    elif dir[0] == "R":
        turns = int(dir[1]/90)
        for _ in range(turns):
            current_dir = (current_dir[1], -current_dir[0])
    else:
        temp_dir = directions[dir[0]]
        d_lat += temp_dir[0]*dir[1]
        d_long += temp_dir[1]*dir[1]

print(d_lat)
print(d_long)
print(abs(d_lat)+abs(d_long))

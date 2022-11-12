#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 13 part 2:
with open("input.txt","r") as infile:
    infile.readline()
    temp = infile.readline().strip().split(",")

times = []
delta = []
prev = 0
for i in range(len(temp)):
    if temp[i] != "x":
        times.append(int(temp[i]))
        delta.append(i)
        prev = i

step = 1
t = 0
i = 0
j = 0
flag = False
while not all([(t + offset) % bus_num == 0 for offset, bus_num in zip(delta, times)]):
    j += 1
    t += step
    if (t + delta[i]) % times[i] == 0:
        if not flag:
            start_step = t
            flag = True
        else:
            flag = False
            step = t - start_step
            i += 1
            print("Step size:", step)

print("Final time:", t)
print("Iterations:", j)

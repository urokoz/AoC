#!/usr/bin/env python3


def bin_to_int(bin):
    num = 0
    for p, i in enumerate(range(len(bin)-1, -1, -1)):
        num += 2**p * int(bin[i])
    return num


infile = open("input.txt", "r")

first = infile.readline().strip()

zeros = [1 if char == "0" else 0 for char in first]
ones = [1 if char == "1" else 0 for char in first]

for line in infile:
    line = line.strip()
    for i, char in enumerate(line):
        if char == "1":
            ones[i] += 1
        else:
            zeros[i] += 1

gam = ""
eps = ""

print("ones:", ones)
print("zeros", zeros)

for o, z in zip(ones, zeros):
    gam += str(int(o > z))
    eps += str(int(o < z))

print(gam)
print(eps)

print(bin_to_int(gam) * bin_to_int(eps))

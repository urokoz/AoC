import math

infile = open("input.txt", "r")

totals = []
total = 0
for line in infile:
    line = line.strip()
    if line == "":
        totals.append(total)
        total = 0
        continue
    total += int(line)

print(sum(sorted(totals)[-3:]))

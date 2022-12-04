

infile = open("input.txt", "r")

totals = []
sum = 0
for line in infile:
    line = line.strip()
    if line == "":
        totals.append(sum)
        sum = 0
        continue
    sum += int(line)

print(max(totals))
    

infile = open("input.txt", "r")

tot = 0

for line in infile:
    line = line.strip()
    split = int(len(line)/2)
    
    comp1 = set(line[:split])
    comp2 = set(line[split:])
    
    miss = list(comp1.intersection(comp2))[0]
    
    if miss.islower():
        tot += ord(miss) - 96
    else:
        tot += ord(miss) - 38
print(tot)
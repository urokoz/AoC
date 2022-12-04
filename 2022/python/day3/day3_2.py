
infile = open("input.txt", "r")

tot = 0
new_f = True
common = {}

for i, line in enumerate(infile, start=1):
    line = line.strip()
    
    if new_f:
        common = set(line)
        new_f = False
    else:
        common = common.intersection(set(line))
    
    if i % 3 == 0:
        badge = list(common)[0]
        
        new_f = True
        
        if badge.islower():
            tot += ord(badge) - 96
        else:
            tot += ord(badge) - 38
print(tot)
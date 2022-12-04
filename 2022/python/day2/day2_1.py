
infile = open(r"C:\Users\uroko\OneDrive\Kodning\AoC\2022\python\day2\input.txt", "r")

# X = 1, Y = 2, Z = 3
# Y > A > Z
# Z > B > X
# X > C > Y

score_guide = {"A": {"X": 1+3, "Y": 2+6, "Z": 3+0},
               "B": {"X": 1+0, "Y": 2+3, "Z": 3+6}, 
               "C": {"X": 1+6, "Y": 2+0, "Z": 3+3}}

total = 0
for line in infile:
    line = line.strip().split()
    
    total += score_guide[line[0]][line[1]]
    
print(total)
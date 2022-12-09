def part1():
    infile = open("input.txt", "r")

    setup_flag = True
    stacks_setup = []

    ship = {}

    for line in infile:
        line = line[:-1]
        if setup_flag:
            if line == "":
                index_row = stacks_setup.pop()
                stacks_setup = stacks_setup[::-1]

                for i, index in enumerate(index_row):
                    if index != " ":
                        stack = [row[i] for row in stacks_setup if row[i] != " "]
                        
                        ship[index] = stack

                setup_flag = False   
                continue                     
            
            stacks_setup.append(line)
        
        else:
            line = line.split()
            
            n = int(line[1])
            
            start = line[3]
            end = line[5]
            
            for _ in range(n):
                temp = ship[start].pop()
                ship[end].append(temp)

    sol = ""
    for k, v in ship.items():
        sol += v[-1]
    print(sol)
    

def part2():
    infile = open("input.txt", "r")

    setup_flag = True
    stacks_setup = []

    ship = {}

    for line in infile:
        line = line[:-1]
        if setup_flag:
            if line == "":
                index_row = stacks_setup.pop()
                stacks_setup = stacks_setup[::-1]

                for i, index in enumerate(index_row):
                    if index != " ":
                        stack = [row[i] for row in stacks_setup if row[i] != " "]
                        
                        ship[index] = stack

                setup_flag = False
                continue                        
            
            stacks_setup.append(line)
        
        else:
            line = line.split()
            
            n = int(line[1])
            
            start = line[3]
            end = line[5]
            
            temp = ship[start][-n:]
            ship[start] = ship[start][:-n]
            ship[end].extend(temp)

    sol = ""
    for k, v in ship.items():
        sol += v[-1]
    print(sol)
    

if __name__ == "__main__":
    print("Part 1:")
    part1()
    print("Part 2:")
    part2()
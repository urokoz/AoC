
def du(dir, infile, dir_sizes):
    
    line = True
    size = 0
    
    while True:
        line = infile.readline()
        
        if line == "":
            break
        
        line = line.strip().split()
        
        if line[0] == "$":
            
            if line[1] == "ls":
                continue
            else:
                new_dir = line[2]
                
                if new_dir == "..":
                    break
                else:
                    new_size, dir_sizes = du(new_dir, infile, dir_sizes)
                    size += new_size
        else:
            if line[0] == "dir":
                continue
            else:
                size += int(line[0])
    dir_sizes.append((dir, size))
    return size, dir_sizes


def part1():
    dir_sizes = []     

    infile = open("input.txt", "r")

    line = infile.readline()

    dir = line.split()[-1]

    tot_size, dir_sizes = du(dir, infile, dir_sizes)
    
    infile.close()

    viable_dirs = [(dir, size) for dir, size in dir_sizes if size <= 100000]

    tot = 0
    for dir, size in viable_dirs:
        tot += size

    print(f"Sum of dirs smaller than 100000: {tot}")

def part2():
    tot_space = 70000000
    space_needed = 30000000
    max_size_for_update = tot_space - space_needed
    
    dir_sizes = []

    infile = open("input.txt", "r")

    line = infile.readline()

    dir = line.split()[-1]

    tot_size, dir_sizes = du(dir, infile, dir_sizes)
    
    infile.close()

    sorted_dirs = sorted(dir_sizes, key=lambda x: x[1])

    for dir, size in sorted_dirs:
        if tot_size - size < max_size_for_update:
            print(f"'{dir}' is the smallest dir that can be deleted for the update.\nSize: {size}")
            break

if __name__ == "__main__":
    part1()
    part2()
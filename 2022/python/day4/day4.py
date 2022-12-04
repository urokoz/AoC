
def part1():
    infile = open("input.txt", "r")

    tot = 0

    for line in infile:
        line = line.split(",")
        elf1 = line[0].split("-")
        elf2 = line[1].split("-")
        
        elf1_low = int(elf1[0])
        elf2_low = int(elf2[0])
        elf1_high = int(elf1[1])
        elf2_high = int(elf2[1])

        if elf1_low >= elf2_low and elf1_high <= elf2_high:
            tot += 1
        elif elf1_low <= elf2_low and elf1_high >= elf2_high:
            tot += 1
    print(tot)


def part2():
    infile = open("input.txt", "r")

    tot = 0

    for line in infile:
        line = line.split(",")
        elf1 = line[0].split("-")
        elf2 = line[1].split("-")

        elf1_low = int(elf1[0])
        elf2_low = int(elf2[0])
        elf1_high = int(elf1[1])
        elf2_high = int(elf2[1])

        if elf1_low <= elf2_high and elf1_high >= elf2_low:
            tot += 1
    print(tot)


if __name__ == "__main__":
    part1()
    part2()
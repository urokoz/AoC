
def part1():
    with open("input.txt", "r") as infile:
        signal = infile.readline()

    for i in range(len(signal)-4):
        temp = signal[i:i+4]
        
        if len(set(temp)) == 4:
            return i+4


def part2():
    with open("input.txt", "r") as infile:
        signal = infile.readline()

    for i in range(len(signal)-14):
        temp = signal[i:i+14]

        if len(set(temp)) == 14:
            return i+14


if __name__ == "__main__":
    print(part1())
    print(part2())
    
    
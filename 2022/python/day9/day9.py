#!/usr/bin/env python3

def addt(a, b) -> tuple:
    return (a[0]+b[0], a[1]+b[1])


def subt(a, b) -> tuple:
    return (a[0]-b[0], a[1]-b[1])


def tail_move(head,tail) -> tuple:
    d = subt(head, tail)
    
    # if max(map(abs, d)) > 1:
    #     move = (d[0]//max(1, abs(d[0])), d[1]//max(1, abs(d[1])))
    #     return addt(tail, move)
    # else:
    #     return tail
    
    if abs(d[0]) > 1 and abs(d[1]) > 1:
        d = (int(d[0]/abs(d[0])),int(d[1]/abs(d[1])))
        tail = addt(tail, d)
    elif abs(d[0]) > 1:
        d = (int(d[0]/abs(d[0])), d[1])
        tail = addt(tail, d)
    elif abs(d[1]) > 1:
        d = (d[0], int(d[1]/abs(d[1])))
        tail = addt(tail, d)
        
    return tail


def print_tail(tail_path):
    tail_path_x = [x for x, y in tail_path]
    tail_path_y = [y for x, y in tail_path]
    
    for i in range(max(tail_path_y), min(tail_path_y)-1, -1):
        for j in range(min(tail_path_x), max(tail_path_x)+1):
            if (j,i) in tail_path:
                print("#", end="")
            else:
                print(".", end="")
        print()


def print_rope(rope):
    home = [(0,0)]
    rope = rope + home
    
    tail_path_x = [x for x, y in rope]
    tail_path_y = [y for x, y in rope]
    plot = []
    line = ""
    
    for _ in range(min(tail_path_y), max(tail_path_y)+1):
        plot.append(["." for _ in range(min(tail_path_x), max(tail_path_x)+1)])
    
    i = 11
    for knot in rope[::-1]:
        i -= 1
        if i == 10:
            mark = "s"
        elif i == 0:
            mark = "H"
        else:
            mark = str(i)
        x = knot[0] - min(tail_path_x)
        y = knot[1] - min(tail_path_y)
        plot[y][x] = mark
    
    for line in plot[::-1]:
        print("".join(line))
    print()
        
        
def part1():
    infile = open("input.txt", "r")

    head, tail = (0,0), (0,0)
    tail_positions = set()
    dirct = {"U": (0,1), "D": (0,-1), "R": (1,0), "L": (-1,0)}

    for line in infile:
        dir, steps = line.strip().split()
        
        for _ in range(int(steps)):
            head = addt(head, dirct[dir])
            tail = tail_move(head, tail)
            tail_positions.add(tail)

    print("Part 1 tail positions:", len(tail_positions))
        
        
def part2():
    infile = open("input.txt", "r")

    rope = [(0,0) for _ in range(10)]
    tail_positions = set()
    dirct = {"U": (0,1), "D": (0,-1), "R": (1,0), "L": (-1,0)}

    for line in infile:
        dir, steps = line.strip().split()
        
        for _ in range(int(steps)):
            rope[0] = addt(rope[0], dirct[dir])
            for i in range(9):
                rope[i+1] = tail_move(rope[i], rope[i+1])
            tail_positions.add(rope[9])
        
    print("Part 2 tail positions:", len(tail_positions))


if __name__ == "__main__":
    part1()
    part2()
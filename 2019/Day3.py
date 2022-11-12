import numpy as np
import pandas as pd


wire1 = np.array((pd.read_csv("3-1.csv", header=None)))[0]
wire2 = np.array((pd.read_csv("3-1.csv", header=None)))[1]


def manhat_dist_ori(cross):
    sdist = min([abs(coors[0]) + abs(coors[1]) for coors in cross])
    return sdist


def walk(wire):
    path = {}
    x, y, count = 0, 0, 0

    for move in wire:
        for _ in range(int(move[1:])):
            if move[0] == "R":
                x += 1
                count += 1
                path[(x, y)] = count
            elif move[0] == "L":
                x -= 1
                count += 1
                path[(x, y)] = count
            elif move[0] == "U":
                y += 1
                count += 1
                path[(x, y)] = count
            elif move[0] == "D":
                y -= 1
                count += 1
                path[(x, y)] = count
    return path


path1 = walk(wire1)
path2 = walk(wire2)

cross = list(path1.keys() & path2.keys())

short_dist = manhat_dist_ori(cross)
print(short_dist)

min_steps = min([path1[coors] + path2[coors] for coors in cross])
print(min_steps)

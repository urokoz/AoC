import numpy as np
import pandas as pd


keys = np.array((pd.read_csv("day6.txt", delimiter=")", header=None)))[:, 1]
vals = np.array((pd.read_csv("day6.txt", delimiter=")", header=None)))[:, 0]
orbits = 0
dict = dict(zip(keys, vals))


def traverse(start, o_map):
    global orbits
    index = start
    while index != "COM":
        orbits += 1
        index = o_map[index]
    return


for i in dict.keys():
    traverse(i, dict)

print(orbits)

you_orbit = 0
san_orbit = 0
you_path = {}
san_path = {}

index = "YOU"
while index != "COM":
    index = dict[index]
    you_orbit += 1
    you_path[index] = you_orbit

index = "SAN"
while index != "COM":
    index = dict[index]
    j = 0
    if index in you_path and j==0:
        first_mutual = san_orbit
    if index in you_path:
        j += 1

    san_orbit += 1
    san_path[index] = you_orbit

len_mutual = len(list(san_path.keys() & you_path.keys()))

you_to_san = san_orbit + you_orbit - 2*len_mutual
print(you_to_san)








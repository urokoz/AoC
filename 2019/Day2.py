import numpy as np
import pandas as pd


raw = np.array((pd.read_csv("2-1.csv", header=None)))[0]


def intcode(noun, verb, raw):
    IC = np.copy(raw)

    IC[1] = noun
    IC[2] = verb

    i = 0
    while i < len(IC):
        if IC[i] == 99:
            break
        if IC[i] == 1:
            IC[IC[i + 3]] = IC[IC[i + 1]] + IC[IC[i + 2]]
            i = i + 4
        elif IC[i] == 2:
            IC[IC[i + 3]] = IC[IC[i + 1]] * IC[IC[i + 2]]
            i = i + 4

    return IC[0]


for i in range(100):
    for j in range(100):
        try:
            a = intcode(i, j, raw)
        except:
            pass
        if a == 19690720:
            v = j
            break
    if a == 19690720:
        n = i
        break

print(n*100 + v)

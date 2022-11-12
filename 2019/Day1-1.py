import numpy as np
import pandas as pd
from math import floor

mass = np.array((pd.read_csv("1-1.csv", header=None)))

a = mass
b = 0
fuel = np.zeros(len(mass))

for i in range(len(mass)):
    c = a[i]
    while True:
        b = floor(c/3)-2
        if b <= 0:
            break
        fuel[i] = fuel[i] + b
        c = b

fFuel = np.sum(fuel)

print(fFuel)


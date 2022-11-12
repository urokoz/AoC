import numpy as np


def mseries(x,N):
    f = 0
    for i in range(1, N+1):
        f = f + (((-1)**(i+1))/i)*x**i
    return f


print(mseries(0.5, 5))

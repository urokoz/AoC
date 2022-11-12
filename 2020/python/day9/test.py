#!/usr/bin/env python3

list = [i for i in range(25)]

for i in range (25):
    splice = list[:i] + list[i+1:]
    print(splice)

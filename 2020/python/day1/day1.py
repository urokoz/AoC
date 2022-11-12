#!/usr/bin/env python3

def sum2020(lst):
    for i in lst:
        for j in lst:
            for k in lst:
                if i + j + k == 2020:
                    return i, j, k

infile = open("input.txt", "r")

num_list = []
for line in infile:
    num_list.append(float(line))

infile.close()

num1, num2, num3 = sum2020(num_list)

print(num1*num2*num3)

#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 9 part 1:

infile = open("input.txt","r")

nums = [int(line) for line in infile]

list = nums[:25]
products = []
for i in range(len(list)):
    list2 = list[:i] + list[i+1:]

    products += [list[i]+j for j in list2]

for new in nums[25:]:
    if new not in products:
        no_fit = new
        break
    else:
        list = list[1:]
        products = products[24:] + [new+i for i in list]
        list.append(new)

print(no_fit)

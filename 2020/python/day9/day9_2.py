#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 9 part 2:

infile = open("input.txt","r")

nums = [int(line) for line in infile]

list = nums[:25]
products = []
for i in range(len(list)):
    list2 = list[:i] + list[i+1:]

    products += [list[i]+j for j in list2]

for j, new in enumerate(nums[25:]):
    if new not in products:
        no_fit = new
        idx = j + 25
        break
    else:
        list = list[1:]
        products = products[24:] + [new+i for i in list]
        list.append(new)

csum = 0
i = 0
j = 2
success = False
while i < idx and not success:
    while csum < no_fit and not success:
        cset = nums[i:j]
        csum = sum(cset)
        if csum == no_fit:
            success = True
        j += 1
    i += 1
    j = i+2
    csum = 0

print(max(cset)+min(cset))

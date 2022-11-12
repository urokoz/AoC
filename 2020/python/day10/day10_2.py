#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 10 part 2:

# A reminder that recursion is bad
# def permutations(dict, jolt=0, counter=0):
#     jumps = dict.get(jolt)
#
#     if jumps:
#         for jump in jumps:
#             counter = permutations(dict, jump, counter)
#     else:
#         counter += 1
#         if counter % 1000000 == 0:
#             print(counter)
#
#     return counter


infile = open("input.txt", "r")

list = [0]+[int(line) for line in infile]   # include 0 as start

list = sorted(list)
jump_dict = dict()
for i in range(1, len(list)):
    connection_list = [list[i-3]]+[list[i-2]]+[list[i-1]] # Only prev 3 vals can fulfill condition

    jump_dict[list[i]] = [j for j in connection_list if list[i]-j in (1,2,3)]     # dict of connections for node i

res_dict = {0:1}
for i in list[1:]:
    res_dict[i] = sum([res_dict[j] for j in jump_dict[i]])  # dict of paths up given node


print(res_dict[max(list)])

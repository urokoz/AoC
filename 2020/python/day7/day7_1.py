#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 7 part 1:
import re
infile = open("input.txt","r")

bag_dict = {}

for line in infile:
    REsult = re.search(r"([\w ]+) bags contain ([\d\w+, ]+)", line)

    if REsult:
        outer = REsult.group(1)
        inner = REsult.group(2).split(",")

        for bag_type in inner:
            colors = re.search(r"\d+ ([\w ]+) bag", bag_type)

            if colors:
                inner_color = colors.group(1)

                if inner_color in bag_dict.keys():
                    bag_dict[inner_color] += [outer]
                else:
                    bag_dict[inner_color] = [outer]
query = "shiny gold"
query_set = set(bag_dict[query])
search_set = set(bag_dict[query])
prev_len = 0
while len(query_set) > prev_len:
    prev_len = len(query_set)
    inter_set = set()
    for color in search_set:
        present_in = bag_dict.get(color, [])
        inter_set.update(present_in)
    search_set = inter_set
    query_set.update(inter_set)

print(prev_len)

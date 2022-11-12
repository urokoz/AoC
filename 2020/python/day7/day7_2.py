#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 7 part 2:
import re

def sum_children(color, dict):
    bags = 1
    children = dict.get(color)

    if children:
        # print("{}: {}".format(color, children))
        for inner_color in children:
            bags += inner_color[1]*sum_children(inner_color[0], dict)
    return bags


infile = open("input.txt","r")

bag_dict = {}
for line in infile:
    REsult = re.search(r"([\w ]+) bags contain ([\d\w+, ]+)", line)

    if REsult:
        outer = REsult.group(1)
        inner = REsult.group(2).split(",")

        inter_list = []
        for bag_type in inner:
            colors = re.search(r"(\d+) ([\w ]+) bag", bag_type)
            if colors:
                inter_list.append((colors.group(2), int(colors.group(1))))

        bag_dict[outer] = inter_list

print(sum_children("shiny gold", bag_dict)-1)

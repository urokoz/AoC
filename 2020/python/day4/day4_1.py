#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 4 part 1:
import re


infile = open("input.txt", "r")

valid_fields = 0
valid_passports = 0
for line in infile:
    byr = re.search(r"byr:", line)
    if byr:
        valid_fields += 1

    iyr = re.search(r"iyr:", line)
    if iyr:
        valid_fields += 1

    eyr = re.search(r"eyr:", line)
    if eyr:
        valid_fields += 1

    hgt = re.search(r"hgt:", line)
    if hgt:
        valid_fields += 1

    hcl = re.search(r"hcl:", line)
    if hcl:
        valid_fields += 1

    ecl = re.search(r"ecl:", line)
    if ecl:
        valid_fields += 1

    pid = re.search(r"pid:", line)
    if pid:
        valid_fields += 1

    # cid = re.search(r"cid:", line)
    # if cid:
    #     valid_fields += 1

    if line.strip() == "":
        if valid_fields == 7:
            valid_passports += 1
        valid_fields = 0

if valid_fields != 0:
    if valid_fields == 7:
        valid_passports += 1

print(valid_passports)

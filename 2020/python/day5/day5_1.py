#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 5 part 1:

infile = open("input.txt", "r")

top_seat_id = 0
for line in infile:
    ticket = line.strip()
    row = ticket[:7]
    seat = ticket[7:]

    row_num = 0
    for i, char in enumerate(row[::-1]):
        if char == "B":
            row_num += 2**i

    seat_num = 0
    for i, char in enumerate(seat[::-1]):
        if char == "R":
            seat_num += 2**i

    seat_id = row_num*8 + seat_num

    if seat_id > top_seat_id:
        top_seat_id = seat_id

print(top_seat_id)

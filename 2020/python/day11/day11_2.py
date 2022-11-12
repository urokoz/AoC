#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 11 part 2:
def neighbor_counter(i,j,matrix):
    """ Checks in all 8(0-7) directions til L or # is found.
        Directions:

        701
        6X2
        543
    """
    dim_i = len(matrix)
    dim_j = len(matrix[0])
    neighbors = 0
    for dir in range(8):
        i_n = i
        jn = j
        while True:
            if dir == 0:
                jn -= 1
            elif dir == 1:
                jn -= 1
                i_n += 1
            elif dir == 2:
                i_n += 1
            elif dir == 3:
                jn += 1
                i_n += 1
            elif dir == 4:
                jn += 1
            elif dir == 5:
                jn += 1
                i_n -= 1
            elif dir == 6:
                i_n -= 1
            elif dir == 7:
                jn -= 1
                i_n -= 1

            if i_n < 0 or jn < 0 or i_n >= dim_i or jn >= dim_j:    # Out of bounds
                break
            elif matrix[i_n][jn] == "L":
                break
            elif matrix[i_n][jn] == "#":
                neighbors += 1
                break

    return neighbors


def matrix_print(matrix):
    """ Parameter: matrix/list of lists/2D array.
        Prints matrix rows on lines in outfile as tab-separated values.
    """
    for row in matrix:
        print("".join([str(elem) for elem in row]))
    print("\n")


infile = open("input.txt")

seating_area = []
neighbor_array = []
for line in infile:
    seating_area.append([char for char in line.strip()])
    neighbor_array.append([0 for char in line.strip()])

changed = True
while changed == True:
    changed = False
    for i, row in enumerate(seating_area):
        for j, seat in enumerate(row):
            if seat == ".":
                continue
            neighbor_array[i][j] = neighbor_counter(i, j, seating_area)

    for i, row in enumerate(seating_area):
        for j, seat in enumerate(row):
            if seat == ".":
                continue
            elif seat == "L" and neighbor_array[i][j] == 0:
                seating_area[i][j] = "#"
                changed = True
            elif seat == "#" and neighbor_array[i][j] >= 5:
                seating_area[i][j] = "L"
                changed = True
    #matrix_print(seating_area)

occupied = 0
for row in seating_area:
    for seat in row:
        if seat == "#":
            occupied += 1
print(occupied)

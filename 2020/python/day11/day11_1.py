#!/usr/bin/env python3
# Author: Mathias Rahbek-Borre
# Advent of code - day 11 part 1:

def neighbor_counter(i,j,matrix):
    dim_i = len(matrix)
    dim_j = len(matrix[0])

    i_n = [k for k in range(i-1,i+2) if k >= 0 and k < dim_i]
    j_n = [k for k in range(j-1,j+2) if k >= 0 and k < dim_j]

    neighbors = 0
    for i2 in i_n:
        for j2 in j_n:
            if i2 != i or j2 != j:
                if matrix[i2][j2] == "#":
                    neighbors += 1
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
    for i in range(len(seating_area)):
        for j in range(len(seating_area[0])):
            neighbor_array[i][j] = neighbor_counter(i,j,seating_area)

    for i in range(len(seating_area)):
        for j in range(len(seating_area[0])):
            if seating_area[i][j] == ".":
                continue
            elif seating_area[i][j] == "L" and neighbor_array[i][j] == 0:
                seating_area[i][j] = "#"
                changed = True
            elif seating_area[i][j] == "#" and neighbor_array[i][j] >= 4:
                seating_area[i][j] = "L"
                changed = True
    matrix_print(seating_area)

occupied = 0
for i in range(len(seating_area)):
    for j in range(len(seating_area[0])):
        if seating_area[i][j] == "#":
            occupied += 1
print(occupied)

import numpy as np

def part1():
    with open("input.txt", "r") as f:
        forrest = f.readlines()
    forrest = np.array([[int(tree) for tree in row.strip()] for row in forrest])

    visible_trees = 0

    for i, row in enumerate(forrest):
        for j, tree in enumerate(row):
            
            if i == 0 or j == 0 or i == len(forrest)-1 or j == len(row)-1:
                visible_trees += 1
                continue
            
            if np.max(forrest[:i, j]) < tree:
                visible_trees += 1
            elif np.max(forrest[i+1:, j]) < tree:
                visible_trees += 1
            elif np.max(forrest[i, :j]) < tree:
                visible_trees += 1
            elif np.max(forrest[i, j+1:]) < tree:
                visible_trees += 1
                
    print("Visible trees from the outside:", visible_trees)


def part2():
    with open("input.txt", "r") as f:
        forrest = f.readlines()
    forrest = np.array([[int(tree) for tree in row.strip()] for row in forrest])

    max_scenic = 0
    for i, row in enumerate(forrest):
        for j, tree in enumerate(row):
            if i == 0 or j == 0 or i == len(forrest)-1 or j == len(row)-1:
                continue            
            
            # look up
            for trees_up, new_tree in enumerate(forrest[:i, j][::-1], start=1):
                if new_tree >= tree:
                    break
            # look down
            for trees_down, new_tree in enumerate(forrest[i+1:, j], start=1):
                if new_tree >= tree:
                    break
            # look up
            for trees_left, new_tree in enumerate(forrest[i, :j][::-1], start=1):
                if new_tree >= tree:
                    break
            # look down
            for trees_right, new_tree in enumerate(forrest[i, j+1:], start=1):
                if new_tree >= tree:
                    break
            
            scenic_score = trees_up*trees_down*trees_left*trees_right
            max_scenic = max(max_scenic, scenic_score)
            
    print("Max scenic score:", max_scenic)


if __name__ == "__main__":
    part1()
    part2()
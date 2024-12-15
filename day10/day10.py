def read_input():
    grid = []
    with open("./input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            tmp = []
            for c in line:
                tmp.append(int(c))

            grid.append(tmp)
        return grid

def find_next_elev(grid, i, j, prev_val):
    # out of grid
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 0
    if grid[i][j] == -1:
        return 0

    curr_val = grid[i][j]
    # reach the peak
    if prev_val == 8 and curr_val == 9:
        grid[i][j] = -1 # no allow for second visit for this starting point 
        return 1
    
    elif curr_val != prev_val + 1:
        return 0
    
    else:
        # mark visited
        grid[i][j] = -1
        u = find_next_elev(grid, i-1, j, curr_val)
        d = find_next_elev(grid, i+1, j, curr_val)
        r = find_next_elev(grid, i, j+1, curr_val)
        l = find_next_elev(grid, i, j-1, curr_val)
        # restore visit
        grid[i][j] = curr_val
        return u + d + r + l

import copy
def solve_part1(grid):
    memo = {}
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # valid start
            if grid[i][j] == 0:
                paths = find_next_elev(copy.deepcopy(grid), i, j, -1)
                total += paths
                #print(f"Searching {i}, {j}... found {paths}")
    print(f"Total ways to reach peaks {total}")

def find_next_elev_distinct(grid, i, j, prev_val):
    # out of grid
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 0
    if grid[i][j] == -1:
        return 0

    curr_val = grid[i][j]
    # reach the peak
    if prev_val == 8 and curr_val == 9:
        return 1
    
    elif curr_val != prev_val + 1:
        return 0
    
    else:
        # mark visited
        grid[i][j] = -1
        u = find_next_elev_distinct(grid, i-1, j, curr_val)
        d = find_next_elev_distinct(grid, i+1, j, curr_val)
        r = find_next_elev_distinct(grid, i, j+1, curr_val)
        l = find_next_elev_distinct(grid, i, j-1, curr_val)
        # restore visit
        grid[i][j] = curr_val
        return u + d + r + l

def solve_part2(grid):
    memo = {}
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # valid start
            if grid[i][j] == 0:
                paths = find_next_elev_distinct(copy.deepcopy(grid), i, j, -1)
                total += paths
                #print(f"Searching {i}, {j}... found {paths}")
    print(f"Total distinct ways to reach peaks {total}")


if __name__ == "__main__":
    grid = read_input()
    solve_part1(grid)
    solve_part2(grid)

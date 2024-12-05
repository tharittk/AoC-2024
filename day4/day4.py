# By Tharit T. | Dec 5, 2024

def read_input():
    grid = []
    with open("./input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            grid.append([c for c in line.strip()])
    return grid

# XMAS needs at least 3 offsets
def search_N(grid, row, col):
    if row - 3 < 0:
        return 0
    if grid[row-1][col] == "M" and grid[row-2][col] == "A" and grid[row-3][col] == "S":
        return 1
    else:
        return 0

def search_NE(grid, row, col):
    if row - 3 < 0 or col + 3 >= len(grid[0]) :
        return 0
    if grid[row-1][col+1] == "M" and grid[row-2][col+2] == "A" and grid[row-3][col+3] == "S":
        return 1
    else:
        return 0

def search_E(grid, row, col):
    if col + 3 >= len(grid[0]) :
        return 0
    if grid[row][col+1] == "M" and grid[row][col+2] == "A" and grid[row][col+3] == "S":
        return 1
    else:
        return 0

def search_SE(grid, row, col):
    if row + 3 >= len(grid) or col + 3 >= len(grid[0]) :
        return 0
    if grid[row+1][col+1] == "M" and grid[row+2][col+2] == "A" and grid[row+3][col+3] == "S":
        return 1
    else:
        return 0

def search_S(grid, row, col):
    if row + 3 >= len(grid) :
        return 0
    if grid[row+1][col] == "M" and grid[row+2][col] == "A" and grid[row+3][col] == "S":
        return 1
    else:
        return 0

def search_SW(grid, row, col):
    if row + 3 >= len(grid) or col - 3 < 0 :
        return 0
    if grid[row+1][col-1] == "M" and grid[row+2][col-2] == "A" and grid[row+3][col-3] == "S":
        return 1
    else:
        return 0

def search_W(grid, row, col):
    if col - 3 < 0 :
        return 0
    if grid[row][col-1] == "M" and grid[row][col-2] == "A" and grid[row][col-3] == "S":
        return 1
    else:
        return 0

def search_NW(grid, row, col):
    if row - 3 < 0 or col - 3 < 0 :
        return 0
    if grid[row-1][col-1] == "M" and grid[row-2][col-2] == "A" and grid[row-3][col-3] == "S":
        return 1
    else:
        return 0

def search_8(grid, row, col):
    return search_N(grid, row, col) + search_NE(grid, row, col) + search_E(grid, row, col) + search_SE(grid, row, col) + search_S(grid, row, col) + search_SW(grid, row, col) + search_W(grid, row, col) + search_NW(grid, row, col)

def solve_part1(grid):
    total_xmas = 0
    for irow in range(len(grid)):
        for icol in range(len(grid[0])):
            if grid[irow][icol] == 'X':
                total_xmas += search_8(grid, irow, icol)

    print(f"Total XMAS: {total_xmas}")

def can_do_x(grid, row, col):
    if row - 1 < 0 or row + 1 >= len(grid) or col - 1 < 0 or col + 1 >= len(grid[0]):
        return False
    else:
        return True

def check_left_diag(grid, row, col):
    return (grid[row-1][col-1] == 'M' and grid[row+1][col+1] == 'S') or (grid[row-1][col-1] == 'S' and grid[row+1][col+1] == 'M')


def check_right_diag(grid, row, col):
    return (grid[row-1][col+1] == 'M' and grid[row+1][col-1] == 'S') or (grid[row-1][col+1] == 'S' and grid[row+1][col-1] == 'M')

def solve_part2(grid):
    total_x_mas = 0
    for irow in range(len(grid)):
        for icol in range(len(grid[0])):
            if grid[irow][icol] == 'A' and can_do_x(grid, irow, icol):
                if check_left_diag(grid, irow, icol) and check_right_diag(grid, irow, icol):
                    total_x_mas += 1
    print(f"Total X-MAS: {total_x_mas}")

if __name__ == "__main__":

    grid = read_input()

    solve_part1(grid)
    solve_part2(grid)

def read_input():
    grid = []
    movements = []
    with open("./input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            if line.startswith("#"):
                grid.append([c for c in line])
            elif line.startswith("\n"):
                continue
            else:
                for m in line:
                    movements.append(m) 
    #print(grid)
    #print(movements)

    return grid, movements

def get_robot_pos(grid):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "@":
                return i, j


def print_grid(grid):
    for row in grid:
        print("\n", end="")
        for col in row:
            print(col, end="")
    print()

# return dx dy
def ingest_move(movement):
    if movement == ">":
        return 1,0
    elif movement == "^":
        return 0,-1
    elif movement == "<":
        return -1,0
    elif movement == "v":
        return 0,1
    else:
        print("Warning ... Movement invalid")

def move_robot(grid, rx, ry, movement):
    dx, dy = ingest_move(movement)

    rx_next = rx+dx
    ry_next = ry+dy

    # space available
    if grid[ry_next][rx_next] == ".":
        grid[ry_next][rx_next] = "@"
        grid[ry][rx] = "."
        return rx_next, ry_next

    # hit the box
    elif grid[ry_next][rx_next] == "O":
        ok = move_box(grid, rx_next, ry_next, dx, dy)
        if ok:
            grid[ry_next][rx_next] = "@"
            grid[ry][rx] = "."
            return rx_next, ry_next
        else:
            return rx, ry
    # hit wall
    elif grid[ry_next][rx_next] == "#":
        return rx, ry
    else:
        print("Warning move robot invalid")
        return rx, ry

def move_box(grid, bx, by, dx, dy):
   
    bx_next = bx+dx
    by_next = by+dy
    
    # space available
    if grid[by_next][bx_next] == ".":
        grid[by_next][bx_next] = "O"
        grid[by][bx] = "."
        return True

    # blocked by another box. Recusrse
    elif grid[by_next][bx_next] == "O":
        ok = move_box(grid, bx_next, by_next, dx, dy)
        if ok:
            grid[by_next][bx_next] = "O"
            grid[by][bx] = "."
            return True
        else:
            return False
    
    # hit the wall
    elif grid[by_next][bx_next] == "#":
        return False
 
    # Should not be here
    else:
        print("Warning.. move box unhandled case")
        return False

def solve_part1(grid, movements, rx, ry):
    for movement in movements:
        rx, ry = move_robot(grid, rx, ry, movement)

    gps_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                gps_score += (100 * i) + j
    print(f"Part 1: GPS score is {gps_score}")
    return gps_score

if __name__ == "__main__":
    grid, movements = read_input()
    rx, ry = get_robot_pos(grid)
    solve_part1(grid, movements, rx, ry)

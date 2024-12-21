def read_input():
    grid = []
    movements = []
    with open("./sinput.txt") as f:
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

def double_grid(grid):
    new_grid = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                row.append('#')
                row.append('#')
            elif grid[i][j] == ".":
                row.append('.')
                row.append('.')
            elif grid[i][j] == "O":
                row.append('[')
                row.append(']')
            elif grid[i][j] == "@":
                print("Detect src", i, j)
                row.append('@')
                row.append('.')
        new_grid.append(row[:])
    return new_grid

def move_robot2(grid, rx, ry, movement):
    dx, dy = ingest_move(movement)
    rx_next = rx+dx
    ry_next = ry+dy

    # space available
    if grid[ry_next][rx_next] == ".":
        grid[ry_next][rx_next] = "@"
        grid[ry][rx] = "."
        return rx_next, ry_next

    # hit the box
    elif grid[ry_next][rx_next] == "[" or grid[ry_next][rx_next] == "]":
        ok = move_box2(grid, rx_next, ry_next, dx, dy)
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

def move_box2(grid, bx, by, dx, dy):
   
    bx_next = bx+dx
    by_next = by+dy
    
    bx_next2 = bx+2*dx
    by_next2 = by+2*dy
    
    # move up/down - easy
    if dx == 0:
        # push from left-side
        if grid[by][bx] == '[':
            # space available
            if grid[by_next][bx_next] == '.' and grid[by_next][bx_next+1] =='.':
                grid[by_next][bx_next] = '['
                grid[by_next][bx_next+1] = ']'
                grid[by][bx] = '.'
                grid[by][bx+1] = '.'
                return True
            # blocked by wall
            elif grid[by_next][bx_next] == '#' or grid[by_next][bx_next+1] =='#':
                return False
            else:
                # []  [][]
                # []   []
                direct_is_box = grid[by_next][bx_next] == '['
                left_side_is_box = grid[by_next][bx_next]== ']'
                right_side_is_box = grid[by_next][bx_next+1] == '['
                        
                if direct_is_box:
                    ok_central = move_box2(grid, bx_next, by_next, dx, dy)
                else:
                    ok_central = False
                if left_side_is_box:
                    ok_left = move_box2(grid, bx_next, by_next, dx, dy)
                else:
                    ok_left = True
                if right_side_is_box:
                    ok_right = move_box2(grid, bx_next+1, by_next, dx, dy)
                else:
                    ok_right = True
                
                # ok both
                if ok_central or (ok_left and ok_right):
                    grid[by_next][bx_next] = '['
                    grid[by_next][bx_next+1] = ']'
                    grid[by][bx] = '.'
                    grid[by][bx+1] = '.'
                    return True
                else:
                    if ok_central:
                        grid[by_next+dy][bx_next] = '.'
                        grid[by_next+dy][bx_next+1] = '.'
                        grid[by_next][bx_next] = '['
                        grid[by_next][bx_next+1] = ']'
                    if ok_left:
                        grid[by_next+dy][bx_next] = '.'
                        grid[by_next+dy][bx_next-1] = '.'
                        grid[by_next][bx_next] = ']'
                        grid[by_next][bx_next-1] = '['
                    if ok_right:
                        grid[by_next+dy][bx_next+1] = '.'
                        grid[by_next+dy][bx_next+2] = '.'
                        grid[by_next][bx_next+1] = '['
                        grid[by_next][bx_next+2] = ']'
                    return False
        # push from right-side
        elif grid[by][bx] == ']':
            # space available
            if grid[by_next][bx_next] == '.' and grid[by_next][bx_next-1] =='.':
                grid[by_next][bx_next] = ']'
                grid[by_next][bx_next-1] = '['
                grid[by][bx] = '.'
                grid[by][bx-1] = '.'
                return True
            # blocked by wall
            elif grid[by_next][bx_next] == '#' or grid[by_next][bx_next-1] =='#':
                return False
            else:
                # []  [][]
                # []   []
                direct_is_box = grid[by_next][bx_next] == ']'
                left_side_is_box = grid[by_next][bx_next-1]== ']'
                right_side_is_box = grid[by_next][bx_next] == '['
            
                if direct_is_box:
                    ok_central = move_box2(grid, bx_next, by_next, dx, dy)
                else:
                    ok_central = False
                if left_side_is_box:
                    ok_left = move_box2(grid, bx_next-1, by_next, dx, dy)
                else:
                    ok_left = True
                if right_side_is_box:
                    ok_right = move_box2(grid, bx_next, by_next, dx, dy)
                else:
                    ok_right = True
                
                # ok both
                if ok_central or (ok_left and ok_right):
                    grid[by_next][bx_next] = ']'
                    grid[by_next][bx_next-1] = '['
                    grid[by][bx] = '.'
                    grid[by][bx-1] = '.'
                    return True
                else:
                    if ok_central:
                        grid[by_next+dy][bx_next] = '.'
                        grid[by_next+dy][bx_next+1] = '.'
                        grid[by_next][bx_next] = ']'
                        grid[by_next][bx_next-1] = '['
                    if ok_left:
                        grid[by_next+dy][bx_next-2] = '.'
                        grid[by_next+dy][bx_next-1] = '.'
                        grid[by_next][bx_next-2] = '['
                        grid[by_next][bx_next-1] = ']'
                    if ok_right:
                        grid[by_next+dy][bx_next] = '.'
                        grid[by_next+dy][bx_next+1] = '.'
                        grid[by_next][bx_next] = '['
                        grid[by_next][bx_next+1] = ']'
                    return False
        else:
            print("Warning .. should not be here in push box up/down")
            return False

    # move right/left
    else:

        # space available
        if grid[by_next2][bx_next2] == ".":
            if dx == -1:
                grid[by_next][bx_next] = ']'
                grid[by_next2][bx_next2] = '['
            elif dx == 1:
                grid[by_next][bx_next] = '['
                grid[by_next2][bx_next2] = ']'
            grid[by][bx] = '.'
            return True
        
        # blocked by another box. Recusrse
        elif grid[by_next2][bx_next2] == "[" or grid[by_next2][bx_next2] == "]":
            ok = move_box2(grid, bx_next2, by_next2, dx, dy)
            if ok:
                if dx == -1:
                    grid[by_next][bx_next] = ']'
                    grid[by_next2][bx_next2] = '['
                elif dx == 1:
                    grid[by_next][bx_next] = '['
                    grid[by_next2][bx_next2] = ']'
                grid[by][bx] = '.'
                return True
            else:
                return False
    
        # hit the wall
        elif grid[by_next2][bx_next2] == "#":
            return False
 
        # Should not be here
        else:
            print("Warning.. move box unhandled case")
            return False


def solve_part2(grid2, movements, rx, ry):
    for movement in movements:
        rx, ry = move_robot2(grid2, rx, ry, movement)
        #print("Movement: ", movement)
        #print_grid(grid2)
    gps_score = 0
    for i in range(len(grid2)):
        for j in range(len(grid2[0])):
            if grid2[i][j] == "[":
                gps_score += (100 * i) + j
    print(f"Part 2: gps score :: {gps_score}")
    return gps_score


if __name__ == "__main__":
    grid, movements = read_input()
    #rx, ry = get_robot_pos(grid)
    #solve_part1(grid, movements, rx, ry)
    grid2 = double_grid(grid)
    print_grid(grid2)
    ry2, rx2 = get_robot_pos(grid2)
    #print(f"Part2 rx {rx2}, ry {ry2}" )
    solve_part2(grid2, movements, rx2, ry2)
    print_grid(grid2)


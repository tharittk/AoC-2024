# By Tharit T. | Dec 6, 2024

def read_input():
    area = []
    with open("./input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            row = []
            for c in line.strip():
                if c == "^":
                    start_y = len(area)
                    start_x = len(row)
                row.append(c)
            area.append(row)
    return area, start_x, start_y

def solve_part1(area, x0, y0):
    nrow = len(area)
    ncol = len(area[0])
    
    # start from heading north
    dx = 0
    dy = -1

    pos_count = 1
    area[y0][x0] = 'X'
    while x0 + dx >= 0 and x0 + dx  < ncol and y0 + dy  >= 0 and y0 + dy < nrow:
    
        xnext, ynext = x0 + dx, y0 + dy

        if area[ynext][xnext] == '#':
            dx, dy = turn_90(dx, dy)
        else:
            x0, y0 = xnext, ynext
            
            if area[y0][x0] != 'X':
                pos_count += 1
                area[y0][x0] = 'X'
    print(f"The guard visits: {pos_count} distinct positions")

def turn_90(dx, dy):
    # north to east
    if dx == 0 and dy == -1:
        return 1, 0
    
    # east to south
    if dx == 1 and dy == 0:
        return 0, 1

    # south to west
    if dx == 0 and dy == 1:
        return -1, 0

    # west to north:
    if dx == -1 and dy == 0:
        return 0, -1

def hit_dir(dx, dy):
    # north
    if dx == 0 and dy == -1:
        return 'N' 
    
    # east
    if dx == 1 and dy == 0:
        return 'E'

    # south
    if dx == 0 and dy == 1:
        return 'S'

    # west
    if dx == -1 and dy == 0:
        return 'W'



def solve_part2(area, x0, y0):
    nrow = len(area)
    ncol = len(area[0])
    
    # start from heading north
    dx = 0
    dy = -1

    x_orig = x0
    y_orig = y0
    # try every point
    valid_pos = 0
    for i in range(ncol):
        print(f"Doing {i} / {ncol}..")
        for j in range(nrow):
            if area[j][i] != '#' and (i,j) != (x_orig, y_orig):
                area[j][i] = 'O'
                hit_history = {}
                x0 = x_orig
                y0 = y_orig
                dx = 0
                dy = -1
            else:
               continue
            while x0 + dx >= 0 and x0 + dx  < ncol and y0 + dy  >= 0 and y0 + dy < nrow:
                
                xnext, ynext = x0 + dx, y0 + dy
                
                # check if hit this box from same face twice
                
                if area[ynext][xnext] == '#' or area[ynext][xnext] == 'O':
                    heading = hit_dir(dx, dy)
    
                    # first time hit
                    if not (xnext, ynext) in hit_history:
                        hit_history[(xnext, ynext)] = []
    
                    if heading in hit_history[(xnext, ynext)]:
                        # loop kicks in
                        valid_pos += 1
                        break
                    else:
                        hit_history[(xnext, ynext)].append(heading)
                        dx, dy = turn_90(dx, dy)
                else:
                    x0, y0 = xnext, ynext
            # reset for next iteration
            area[j][i] = '.'
    print(f"You can place the box in {valid_pos} possible positions")


if __name__ == "__main__":
    area, start_x, start_y = read_input()
    solve_part1(area, start_x, start_y)
    solve_part2(area, start_x, start_y)

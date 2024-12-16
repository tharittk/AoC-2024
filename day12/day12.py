def read_input():
    grid = []
    with open("input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            tmp = []
            for c in line:
                tmp.append(c)
            grid.append(tmp[:])

    return grid

def in_grid(grid, x, y):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0])

def dfs(grid, x ,y, visited, cc):
    visited[y][x] = True
    cc.append((y,x))
    for move in [(-1,0), (1,0), (0,-1), (0,1)]:
        
        dx = move[0]
        dy = move[1]
        
        xnext = x + dx
        ynext = y + dy
        
        if in_grid(grid, xnext, ynext):
            if not visited[ynext][xnext] and grid[ynext][xnext] == grid[y][x]:
                dfs(grid, xnext, ynext, visited, cc)

def connected_component(grid):
    visited = [ [False for i in range(len(grid[0]))] for j in range(len(grid))]
    all_cc = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if not visited[y][x]: 
                    cc = []
                    dfs(grid, x, y, visited, cc)
                    all_cc.append(cc)
    return all_cc

def count_perimeter(cc):
    s = set()
    for p in cc:
        s.add(p)
    perim = 0
    for p in cc:
        y = p[0]
        x = p[1]
        # left
        if (y, x-1) not in s:
            perim += 1
        # right
        if (y, x+1) not in s:
            perim += 1
        # bottom
        if (y+1, x) not in s:
            perim += 1
        # top:
        if (y-1, x) not in s:
            perim += 1
    return perim

def get_price(cc):
    area = len(cc)
    perim = count_perimeter(cc)
    return area * perim

def solve_part1(all_cc):
    total = 0
    for cc in all_cc:
        total += get_price(cc)
    print(f"Part 1 total price: {total}")

def count_face(cc):
    s = set()
    
    face = {}

    for p in cc:
        s.add(p)
    for p in cc:
        y = p[0]
        x = p[1]
        # left
        if (y, x-1) not in s:
            key = str(x) + 'l'
            if key not in face:
                face[key] = [(x,y)]
            else:
                face[key].append((x,y))
        # right
        if (y, x+1) not in s:
            key = str(x) + 'r'
            if key not in face:
                face[key] = [(x,y)]
            else:
                face[key].append((x,y))
        # bottom
        if (y+1, x) not in s:
            key = str(y) + 'b'
            if key not in face:
                face[key] = [(x,y)]
            else:
                face[key].append((x,y))
        # top:
        if (y-1, x) not in s:
            key = str(y) + 't'
            if key not in face:
                face[key] = [(x,y)]
            else:
                face[key].append((x,y))
    return face

def get_price_face(cc):
    area = len(cc)
    face_dict = count_face(cc)
    face = count_distinct_face(face_dict)
    #print(f" area {area} x {face} faces = {area * face}")
    return area * face

def count_distinct_face(face_dict):
    # each key may have many disconnect intervals
    face_count = 0
    for key in face_dict:
        count = 1 # at least it must be one connected group
        pairs = face_dict[key]
        # check x interval
        if key[-1] == 't' or key[-1] == 'b':
            x_list = sorted([p[0] for p in pairs])
            curr = x_list[0]
            for ix in x_list[1:]:
                if ix != curr + 1:
                    count += 1
                curr = ix
        # check y interval
        elif key[-1] == 'r' or key[-1] == 'l':
            y_list = sorted([p[1] for p in pairs])
            curr = y_list[0]
            for iy in y_list[1:]:
                if iy != curr + 1:
                    count += 1
                curr = iy
        else:
            print("must not be here")
        
        face_count += count
        #print(f"Count face for key {key} :", count, "input: ", pairs)
    return face_count
def solve_part2(all_cc):
    total = 0
    for cc in all_cc:
        total += get_price_face(cc)
    print(f"Part 2 total price: {total}")


if __name__ == "__main__":
    grid = read_input()
    all_cc = connected_component(grid)
    solve_part1(all_cc)
    solve_part2(all_cc)

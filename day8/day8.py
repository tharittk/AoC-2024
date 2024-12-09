def read_input():
    grid = []
    with open("./input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            grid.append([c for c in line])

    return grid

def build_key_loc_table(grid):
    key_loc = {}
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            name = grid[row][col]
            if name != ".":
                if not name in key_loc:
                    key_loc[name] = [ (col, row) ]
                else:
                    key_loc[name].append((col ,row))
    return key_loc

def find_all_antinode_loc(antenna_loc):
    
    # set takes care of duplication
    locs = set()

    for i in range(len(antenna_loc)):
        for j in range(i+1, len(antenna_loc)):
            
            antinode_locs = compute_antinode_loc_from_pair( antenna_loc[i], antenna_loc[j] )


            for loc in antinode_locs:
                locs.add(loc)
    return locs

def compute_antinode_loc_from_pair(loc1, loc2):
    dx, dy = loc2[0] - loc1[0], loc2[1] - loc1[1]

    loc1_ext = (loc1[0] + 2 * dx, loc1[1] + 2 * dy)
    loc2_ext = (loc2[0] - 2 * dx, loc2[1] - 2 * dy)
    
    return [loc1_ext, loc2_ext]


def is_in_grid(grid, loc):
    x = loc[1]
    y = loc[0]

    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def solve_part1(grid):

    key_loc = build_key_loc_table(grid)

    # set takes care of duplication
    antinode_locs = set()

    for key in key_loc:
        antenna_loc = key_loc[key]

        locs = find_all_antinode_loc (antenna_loc)
        
        for loc in locs:

            if is_in_grid(grid, loc):
                #print(loc, "is added, ",key)
                antinode_locs.add(loc)
    
    print(f"Unique locations for antinode {len(antinode_locs)}")

    return len(antinode_locs)
 
def find_all_antinode_loc_ext(antenna_loc, grid):
    
    # set takes care of duplication
    locs = set()

    for i in range(len(antenna_loc)):
        for j in range(i+1, len(antenna_loc)):
            
            antinode_locs = compute_antinode_loc_from_pair_ext(antenna_loc[i], antenna_loc[j], grid)

            for loc in antinode_locs:
                locs.add(loc)
    return locs

def compute_antinode_loc_from_pair_ext(loc1, loc2, grid):
    dx, dy = loc2[0] - loc1[0], loc2[1] - loc1[1]
   
    ret = []

    factor = 1
    loc1_ext = (loc1[0] + factor * dx, loc1[1] + factor * dy)
    while is_in_grid(grid, loc1_ext):
        ret.append(loc1_ext)
        factor += 1
        loc1_ext = (loc1[0] + factor * dx, loc1[1] + factor * dy)

    factor = 1
    loc2_ext = (loc2[0] - factor * dx, loc2[1] - factor * dy)
    while is_in_grid(grid, loc2_ext):
        ret.append(loc2_ext)
        factor += 1
        loc2_ext = (loc2[0] - factor * dx, loc2[1] - factor * dy)


    
    return ret

   
def solve_part2(grid):

    key_loc = build_key_loc_table(grid)

    # set takes care of duplication
    antinode_locs = set()

    for key in key_loc:
        antenna_loc = key_loc[key]

        locs = find_all_antinode_loc_ext(antenna_loc, grid)
        
        for loc in locs:
            #print(loc, "is added", key)
            antinode_locs.add(loc)
   

    print(f"Unique locations for antinode wth Harmonic {len(antinode_locs)}")

    return len(antinode_locs)
 
if __name__ == "__main__":
    grid = read_input()
    
    _ = solve_part1(grid)
    _ = solve_part2(grid)

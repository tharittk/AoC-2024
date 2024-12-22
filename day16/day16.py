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
                tmp.append(c)
            grid.append(tmp[:])
        return grid

def get_start_xy(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return j,i 
def get_possible_turn(facing):
    if facing == 'E':
        return [(0, -1, 'N'), (1, 0,'E'), (0, 1,'S')]
    elif facing == 'N':
        return [(-1, 0, 'W'), (1, 0,'E'), (0, -1,'N')]
    elif facing == 'W':
        return [(0,-1,'N'), (-1, 0,'W'), (0, 1,'S')]
    elif facing == 'S':
        return [(0, 1,'S'), (1, 0,'E'), (-1, 0,'W')]

def check_valid_xy(grid, x, y):
    if grid[y][x] == '#':
        return False
    elif y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        return False
    else:
        return True

def find_all_paths_bfs(grid, x0, y0):
    visited = [ [float('inf') for i in range(len(grid[0]))] for j in range(len(grid))]
    q = [(x0, y0, 'E', 0)]
    minScore = float('inf')
    while q:
        x, y, facing, score = q.pop(0)
        if score > visited[y][x]:
            continue
        else:
            visited[y][x] = score

        if grid[y][x] == 'E':
            minScore = score
        turns = get_possible_turn(facing)
        for dx, dy, nextTurn in turns:
            if check_valid_xy(grid, x+dx, y+dy):
                new_score = score + (1001 if nextTurn != facing else 1)
                q.append((x+dx, y+dy, nextTurn, new_score))
    print("Part 1: minScore is: ", minScore)
    return minScore

import heapq
def find_opt_paths(grid, x0, y0):
    visited = [ [float('inf') for i in range(len(grid[0]))] for j in range(len(grid))]
    q = [(x0, y0, 'E', 0, [(x0,y0)])]
    minScore = float('inf')
    pathSet = set()
    while q:
        x, y, facing, score, path = q.pop(0)
        #print(x, y, facing, score, path)
        if score > visited[y][x]:
            continue
        else:
            visited[y][x] = score
        # Check if we've reached the endpoint
        if grid[y][x] == 'E':
            if score < minScore:
                pathSet = set()
                minScore = score
                print("reset pathSet with new minimum score:", minScore)
            for e in path:
                pathSet.add(e)
            print("Current pathSet size:", len(pathSet))
            continue
        turns = get_possible_turn(facing)
        for dx, dy, nextTurn in turns:
            if check_valid_xy(grid, x+dx, y+dy):
                new_score = score + (1001 if nextTurn != facing else 1)
                new_path = [e for e in path]
                new_path.append((x+dx, y+dy))
                #heapq.heappush(q, (x+dx, y+dy, nextTurn, new_score, new_path))
                q.append((x+dx, y+dy, nextTurn, new_score, new_path))
    print("Part2 min Score is:", minScore, "elem in set", len(pathSet))
    return minScore, pathSet

def print_grid(grid, pathSet):
    for j in range(len(grid)):
        for i in range(len(grid[0])):

            if (i, j) in pathSet:
                print("O", end="")
            else:
                if i == len(grid[0]) - 1:
                    print(grid[j][i])
                else: 
                    print(grid[j][i], end="")

if __name__ == "__main__":
    grid = read_input()
    x0, y0 = get_start_xy(grid)
    minScore = find_all_paths_bfs(grid, x0, y0)
    minScore, pathSet = find_opt_paths(grid, x0, y0)

    #print_grid(grid, pathSet)

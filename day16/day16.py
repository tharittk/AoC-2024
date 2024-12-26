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
from heapq import heappush, heappop

def find_opt_paths(grid, x0, y0):
    # visited now tracks both position and direction
    visited = {}  # (x, y, facing) -> score
    # Using priority queue to process lower scores first
    q = [(0, x0, y0, 'E', [(x0,y0)])]
    minScore = float('inf')
    optimal_paths = []
    
    while q:
        #score, x, y, facing, path = heappop(q)
        score, x, y, facing, path = q.pop(0)

        state = (x, y, facing)
        if state in visited and visited[state] < score:
            continue
        visited[state] = score
        
        # Check if we've reached the endpoint
        if grid[y][x] == 'E':
            if score < minScore:
                optimal_paths = [path]
                minScore = score
                print("Found new minimum score:", minScore)
            elif score == minScore:
                optimal_paths.append(path)
            continue
            
        turns = get_possible_turn(facing)
        for dx, dy, nextTurn in turns:
            if check_valid_xy(grid, x+dx, y+dy):
                turn_cost = 1001 if nextTurn != facing else 1
                new_score = score + turn_cost
                new_path = path + [(x+dx, y+dy)]
                
                next_state = (x+dx, y+dy, nextTurn)
                if next_state not in visited or visited[next_state] >= new_score:
                    #heappush(q, (new_score, x+dx, y+dy, nextTurn, new_path))
                    q.append((new_score, x+dx, y+dy, nextTurn, new_path))
    # Convert paths to set of coordinates for compatibility
    pathSet = set()
    for path in optimal_paths:
        pathSet.update(path)
    
    print(f"Part2 min Score is: {minScore}, found {len(optimal_paths)} optimal paths")
    print("Elements in pathSet", len(pathSet))
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
    #minScore = find_all_paths_bfs(grid, x0, y0)
    minScore, pathSet = find_opt_paths(grid, x0, y0)

    #print_grid(grid, pathSet)

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
        return [(0,-1, 'N'), (1,0,'E'), (0,1,'S')]
    elif facing == 'N':
        return [(-1,0, 'W'), (1,0,'E'), (0,-1,'N')]
    elif facing == 'W':
        return [(0,-1, 'N'), (-1,0,'W'), (0,1,'S')]
    elif facing == 'S':
        return [(0,1, 'S'), (1,0,'E'), (-1,0,'W')]

def check_valid_xy(grid, x, y):
    if grid[y][x] == '#':
        return False
    elif y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        return False
    else:
        return True

def find_all_paths(grid, x0, y0):
    visited = [ [False for i in range(len(grid[0]))] for j in range(len(grid))]
    pathScore = []
    memo = {}
    def dfs(grid, x, y, facing, score, visited, minScore,memo):
        if grid[y][x] == 'E':
            minScore[0] = min(minScore[0], score)
            print("So far", minScore)
            return minScore[0]
        if not check_valid_xy(grid, x, y):
            return
        if visited[y][x]:
            return
        if score > minScore[0]:
            return
        else:
            visited[y][x] = True
            turns = get_possible_turn(facing)
            for dx, dy, nextTurn in turns:
                if nextTurn == facing:
                    s = dfs(grid, x+dx, y+dy, nextTurn, score+1, visited, minScore)
                else:
                    s = dfs(grid, x+dx, y+dy, nextTurn, score+1001, visited, minScore)
            visited[y][x] = False
    minScore = [float('inf')]
    dfs(grid, x0, y0, 'E', 0, visited, minScore)
    print("min path score: ", minScore[0]) 
    return pathScore

import sys
if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    grid = read_input()
    x0, y0 = get_start_xy(grid)
    pathScore = find_all_paths(grid, x0, y0)

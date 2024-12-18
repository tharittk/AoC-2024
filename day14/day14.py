import re

def read_input():
    robots = []
    with open("./input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            numbers = re.findall(r"-?\d+", line)
            robots.append([int(s) for s in numbers])
    return robots

def move_robot_n_step(robot, width, height, n):
    x0 = robot[0]
    y0 = robot[1]
    vx = robot[2]
    vy = robot[3]
    for i in range(n):
        x0 = (x0 + vx) % width
        y0 = (y0 + vy) % height
    
    return x0, y0

def move_robot_one_step(robot, width, height):
    x0 = robot[0]
    y0 = robot[1]
    vx = robot[2]
    vy = robot[3]
    
    robot[0] = (x0 + vx) % width
    robot[1] = (y0 + vy) % height
    

def get_quadrant(x, y, width, height):
    cx = width // 2
    cy = height // 2

    if x < cx and y < cy:
        return 4
    elif x < cx and y > cy:
        return 3
    elif x > cx and y < cy:
        return 1
    elif x > cx and y > cy:
        return 2
    else:
        return -1

def solve_part1(robots, width, height):
    q = {1:0, 2:0, 3:0, 4:0, -1:0}
    for robot in robots:
        x,y = move_robot_n_step(robot, width, height, 100)
        iq = get_quadrant(x, y, width, height)
        q[iq] += 1

    print(f"q1: {q[1]}, q2: {q[2]}, q3: {q[3]}, q4: {q[4]}")
    return q[1] * q[2] * q[3] * q[4]

def solve_part2(robots, width, height):
    best_iter = None
    min_safe = float('inf')
    for i in range(width * height):
        q = {1:0, 2:0, 3:0, 4:0, -1:0}
        for robot in robots:
            x,y = move_robot_n_step(robot, width, height, 1)
            robot[0] = x
            robot[1] = y
            iq = get_quadrant(x, y, width, height)
            q[iq] += 1
        safe = q[1] * q[2] * q[3] * q[4]
        if safe < min_safe:
            min_safe = safe
            best_iter = i
        if i == 99:
            print("At 100 sec, ", safe)
    print(f"best iter {best_iter}, min safe {min_safe}")

if __name__ == "__main__":
    robots = read_input()
    width = 101
    height = 103
    multiply = solve_part1(robots, width, height)
    print(f"Part 1: the product is {multiply}")
    solve_part2(robots, width, height)
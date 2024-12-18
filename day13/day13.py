import re

def read_input():
    configs = []
    x_plus_pattern = r"X\+(\d+)"
    y_plus_pattern = r"Y\+(\d+)"
    x_equals_pattern = r"X=(\d+)"
    y_equals_pattern = r"Y=(\d+)"    

    problems = {}
    with open("./sinput.txt") as f:
        lines = f.readlines()
    pid = 0
    for i in range(0, len(lines), 4):
        problems[pid] = {}
        config = problems[pid]
        cfg = ''.join(lines[i: i +3])
        
        xp = re.findall(x_plus_pattern, cfg)
        yp = re.findall(y_plus_pattern, cfg)
        xe = re.findall(x_equals_pattern, cfg)
        ye = re.findall(y_equals_pattern, cfg)

        config['Ax'] = int(xp[0])
        config['Ay'] = int(yp[0])
        config['Bx'] = int(xp[1])
        config['By'] = int(yp[1])
        config['Px'] = int(xe[0])
        config['Py'] = int(ye[0])
        pid += 1
    return problems

def recurse_one_config(config):

    x_final = config['Px']
    y_final = config['Py']
    print(f"recurse with {x_final} {y_final}")
    Ax = config['Ax']
    Ay = config['Ay']
    Bx = config['Bx']
    By = config['By']

    def aux(x_final, y_final, memo):
        if (x_final, y_final) in memo:
            return memo[(x_final, y_final)]
        if x_final==0 and y_final==0:
            return 0
        # infeasible path
        if x_final < 0 or y_final < 0:
            return float('inf')

        cost = min(3 +  aux(x_final-Ax, y_final-Ay, memo), 1 + aux(x_final-Bx, y_final-By, memo))
        memo[(x_final, y_final)] = cost
        return cost
    memo = {}
    cost = aux(x_final, y_final, memo)
    return cost

def solve_part1(problems):
    total = 0
    for key in problems.keys():
        config = problems[key]
        cost = recurse_one_config(config)
        if cost != float('inf'):
            total += cost
        #print(f"Min cost is: {cost}")
    print(f"Part 1 total cost :{total}")

def solve_trillion(config):
    # solve original problem first
    trillion = 1e12
    target_x = config['Px']
    target_y = config['Py']

    c1 = target_x - target_y
    c2 = config['Ax'] - config['Ay']
    c3 = config['Bx'] - config['By']

    print(f"c1: {c1}, c2: {c2}, c3: {c3}")


    # big_x = Bx * c1 / c3 + nA * (Ax- Bx*C2/C3)
    nA = ((trillion + target_x) - (config['Bx'] * c1 / c3)) / (config['Ax'] - (c2*config['Bx']/c3))
    nB = (c1 - nA * c2) / c3

    print(f"Result is nA = {nA} nb = {nB}")

    # infeasibile
    if not nA.is_integer():
        print("Infeasible")
        return float('inf')

    else:
        return 3 * nA + nB

def solve_part2(problems):
    total = 0
    for key in problems.keys():
        config = problems[key]
        cost = solve_trillion(config)
        print(f"Cost is {cost}")
        if cost != float('inf'):
            total += cost


if __name__ == "__main__":
    problems = read_input()
    #solve_part1(problems)
    solve_part2(problems)


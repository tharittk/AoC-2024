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

        print(f"match, xp {xp}, yp {yp}, xe {xe}, ye {ye}")

        config['Ax'] = int(xp[0])
        config['Ay'] = int(yp[0])
        config['Bx'] = int(xp[1])
        config['By'] = int(yp[1])
        config['Px'] = int(xe[0])
        config['Py'] = int(ye[0])
        pid += 1
    return problems

def dp_one_config(config):

    x_final = config['Px']
    y_final = config['Py']

    dp = [[float('inf') for w in range(x_final+1)] for h in range(y_final+1)]

    # zero cost to start
    dp[0][0] = 0

    for dx, dy, cost in [ [config['Ax'], config['Ay'], 3], [config['Bx'], config['By'], 1] ]:
        for i in range(1, x_final+1):
            for j in range(1, y_final+1):
                if i - dx >= 0 and j -dy >= 0:
                    dp[j][i] = min(dp[j][i], dp[j-dy][i-dx] + cost)
    return dp[-1][-1]



if __name__ == "__main__":
    problems = read_input()
    #print(problems)

    for key in problems.keys():
        config = problems[key]
        cost = dp_one_config(config)
        print(f"Min cost is: {cost}")
        break

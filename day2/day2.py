
def read_input():
    reports = []
    with open("./input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            levels = line.strip().split(" ")
            report = [int(i) for i in levels]
            reports.append(report)
    return reports
    
def check_report_ok(report):
    if len(report) == 1:
        return True

    # overall must be decreasing or increasing
    sign = 1 if report[-1] - report[0] > 0 else -1

    for i in range(1,len(report)):
        diff = report[i] - report[i-1]
        grad_sign = 1 if diff >= 0 else -1
        diff = abs(diff)
        
        if (diff >= 1 and diff <= 3) and grad_sign == sign:
            continue
        else:
            return False
    return True



def solve_part1(reports):
    safe_report_count = 0
    for report in reports:
        if check_report_ok (report):
            safe_report_count += 1

    print(f"Total Safe report {safe_report_count}")

def check_report_ok_with_tol(report):
    if len(report) == 1:
        return True

    # overall must be decreasing or increasing
    sign = 1 if report[-1] - report[0] > 0 else -1

    head = 0
    tail = 1

    while tail < len(report):
        diff = report[tail] - report[head]
        grad_sign = 1 if diff >= 0 else -1
        diff = abs(diff)
        
        if (diff >= 1 and diff <= 3) and grad_sign == sign:
            head += 1
            tail += 1
            continue
        else:
            # either deleting the head or tail must succeed
            del_head = check_report_ok(report[:head] + report[head+1:])
            del_tail = check_report_ok(report[:tail] + report[tail+1:])
            if del_head or del_tail:
                return True
            else:
                return False
    return True

def solve_part2(reports):
    safe_report_count = 0
    for report in reports:
        if check_report_ok_with_tol(report):
            safe_report_count += 1
    print(f"Safe report with tol {safe_report_count}")

if __name__ == "__main__":
    reports = read_input()

    solve_part1(reports)

    #solve_part2([[1,3,2,4,5]])
    solve_part2(reports)

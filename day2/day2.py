
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


if __name__ == "__main__":
    reports = read_input()

    solve_part1(reports)
    #print(check_report_ok([7,6,4,2,1]))
    #print(check_report_ok([1,2,7,8,9]))
    #print(check_report_ok([9,7,6,2,1]))

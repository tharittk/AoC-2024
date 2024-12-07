# By Tharit T. | Dec 7, 2024

def read_input():
    results = []
    args = []
    with open("./input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break

            result,  arg = line.strip().split(": ")

            results.append(int(result))

            args.append([int(t) for t in arg.split(" ")])
            
    return results, args

def find_operator(current, target, arg_list):

    # early termination. + and * for positive number only goes up
    if current > target:
        return False

    # success
    if current == target and not arg_list:
        return True

    # exhaust and not reach the result
    if not arg_list:
        return False

    arg = arg_list[0]

    return find_operator(current + arg, target, arg_list[1:]) or find_operator(current * arg, target, arg_list[1:])

def solve_part1(results, args):

    total = 0

    for i in range(len(results)):
        target = results[i]
        arg_list = args[i]

        possible = find_operator(arg_list[0], target, arg_list[1:])

        if possible:
            #print(f"{target} : {arg_list} is possble")
            total += target
    print(f"Sum of all possible equation {total}")

def find_operator_concat(current, target, arg_list):

    # early termination. +, *, and || for positive number only goes up
    if current > target:
        return False

    # success
    if current == target and not arg_list:
        return True

    # exhaust and not reach the result
    if not arg_list:
        return False

    arg = arg_list[0]

    concat_str = str(current) + str(arg)
    concat = int(concat_str)

    return find_operator_concat(current + arg, target, arg_list[1:]) or find_operator_concat(current * arg, target, arg_list[1:]) or find_operator_concat(concat, target, arg_list[1:])


def solve_part2(results, args):

    total = 0

    for i in range(len(results)):
        target = results[i]
        arg_list = args[i]

        possible = find_operator_concat(arg_list[0], target, arg_list[1:])

        if possible:
            #print(f"{target} : {arg_list} is possble")
            total += target

    print(f"Sum of all possible equation with Concat ||{total}")


if __name__ == "__main__":
    results, args = read_input()

    solve_part1(results, args)

    solve_part2(results, args)

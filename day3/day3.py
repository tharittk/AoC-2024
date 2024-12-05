# By Tharit T. | Dec 5, 2024

def read_input():
    with open("./input.txt") as f:
        lines = f.readlines()
    return ''.join(lines)

def match_mul(line, beg):
    '''
    find mul( and return next index to probe
    '''
    while beg < len(line)-3:
        if line[beg:beg+4] == 'mul(':
            return 'mul(', beg + 4
        else:
            beg += 1
    return '', beg

def match_arg1(line, beg):
    '''
    find first argument '#*3,' and return next index to probe
    '''
    arg = ''
    while beg < len(line):
        # found comma
        if len(arg) >= 1 and line[beg] == ",":
            return arg, beg+1

        # keep accumulating
        elif line[beg].isnumeric() and len(arg) < 3:
            arg += line[beg]
            beg += 1
       
       # invalid or cannot accumulate more than 3 digits 
        else:
            return '', beg

    return '', beg
  
def match_arg2(line, beg):
    '''
    find second argument '#*3)' and return next index to probe
    '''
    arg = ''
    while beg < len(line):
        
        # end of arg with valid parenthesis
        if len(arg) >= 1 and line[beg] == ")":
            return arg, beg + 1
        
        # keep accumulating
        elif line[beg].isnumeric() and len(arg) < 3:
            arg += line[beg]
            beg += 1
        
        # invalid or cannot accumulate more than 3 digits
        else:
            return '', beg
    
    return '', beg


def accumulate_args(memory):
    args1 = []
    args2 = []
    beg = 0

    while beg < len(memory):

        _, next_probe = match_mul(memory, beg)
        
        # not enough for two arguments i.e, #,#)
        if len(memory) - next_probe < 4: 
            break

        a1, next_probe = match_arg1(memory, next_probe)
        # start all over
        if not a1:
            beg = next_probe
            continue

        a2, next_probe = match_arg2(memory, next_probe)
        # start all over
        if not a2:
            beg = next_probe
            continue

        # ok
        assert(len(a1) >= 1 and len(a1) <= 3)
        assert(len(a2) >= 1 and len(a2) <= 3)
        args1.append(int(a1))
        args2.append(int(a2))

        beg = next_probe

    return args1, args2
    
def solve_part1(memory):
    args1, args2 = accumulate_args(memory)

    total = do_multiply_and_sum(args1, args2)

    print(f"Add up all Mul: {total}")

def get_index_after_dont(line, beg):
    # don't()
    while beg < len(line)- 6:
        if line[beg: beg +7] == "don't()":
            return "don't()", beg+7
        else:
            beg += 1
    return '', beg

def get_index_after_do(line, beg):
    # do()
    while beg < len(line)- 3:
        if line[beg: beg +4] == "do()":
            return "do()", beg+4
        else:
            beg += 1
    return '', beg

def do_multiply_and_sum(args1, args2):
    total = 0
    for i in range(len(args1)):
        total += int(args1[i]) * int(args2[i])
    return total

def solve_part2(memory):
    do_from = 0
    total = 0

    # the valid compute interval is [do] ... [dont']
    while do_from < len(memory):
       
        # find don't
        c, dont_from = get_index_after_dont(memory, do_from)
        if not c:
            # terminate without don't
            args1, args2 = accumulate_args(memory[do_from:])
            total += do_multiply_and_sum(args1, args2)
            break
        assert(c == "don't()")
        
        args1, args2 = accumulate_args(memory[do_from:dont_from])
        
        total += do_multiply_and_sum(args1, args2)

        # skip what comes after don't until see do

        c, do_from = get_index_after_do(memory, dont_from)
        
        if not c:
            break
        assert(c == "do()")

    print(f"Result after do and don't {total}")

if __name__ == "__main__":
    memory = read_input()

    #tmem = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    solve_part1(memory)

    #tmem2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    
    solve_part2(memory)


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
            #print("found arg1", arg)
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
            #print("found arg2: ", arg)
            return arg, beg + 1
        
        # keep accumulating
        elif line[beg].isnumeric() and len(arg) < 3:
            arg += line[beg]
            beg += 1
        
        else:
            return '', beg
    
    return '', beg


def solve_part1(memory):
    args1 = []
    args2 = []
    beg = 0

    while beg < len(memory):

        _, next_probe = match_mul(memory, beg)
        
        # not enough for #,#)
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

    total = 0
    
    for i in range(len(args1)):
        total += int(args1[i]) * int(args2[i])

    print(f"Add up all Mul: {total}")

if __name__ == "__main__":
    memory = read_input()

    #tmem = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    #solve_part1(tmem)

    solve_part1(memory)


def resolve_operand(state, operand):
    if 0 <= operand <= 3:
        return operand  # Literal value
    elif operand == 4:
        return state['A']
    elif operand == 5:
        return state['B']
    elif operand == 6:
        return state['C']
    else:
        raise ValueError("Invalid operand: 7 is not allowed")

def execute_op(state, opcode, operand):
    jump = False
    match opcode:
        case '0':
            # adv
            state['A'] = state['A'] // (2**operand)
        case '1':
            # bxl
            state['B'] = state['B'] ^ operand
        case '2':
            # bst
            state['B'] = operand % 8
        case '3':
            # jnz
            if state['A'] != 0:
                state['PC'] = operand
                jump = True
        case '4':
            # bxc
            state['B'] = state['B'] ^ state['C']
        case '5':
            # out
            state['OUT'].append(operand % 8)
        case '6':
            # bdv
            state['B'] = state['A'] // (2**operand)
        case '7':
            # cdv
            state['C'] = state['A'] // (2**operand)
        case _:
            print("Default NONE")
    if not jump:
        state['PC'] += 2
def run_program(state, program):
    while state['PC'] < len(program):
        opcode = program[state['PC']]
        operand = program[state['PC'] + 1]
        operand = resolve_operand(state, int(operand))
        execute_op(state, opcode, operand)

        print(state)

if __name__ == "__main__":

    # state = {'A':729, 'B':0, 'C':0, 'PC':0, 'OUT':[]}
    # program = '015430'
   
    # part 1 config
    state = {'A':21539243, 'B':0, 'C':0, 'PC':0, 'OUT':[]}
    program = '2413751503415530'
    run_program(state, program)

    print("Result join: ", ''.join([str(c) for c in state['OUT']]))

def read_input():
    stones = []
    with open("./input.txt") as f:
        line = f.readline()
        line = line.strip()
        line = line.split(" ")
        for num in line:
            stones.append(num)
    #print(stones)
    return stones

def blink(stone: str):

    if int(stone) == 0:
        return ['1']
    elif int(stone) == '1':
        return ['2024']
    elif len(stone) % 2 == 0:
        first = stone[:len(stone)//2]
        second = stone[len(stone)//2:]
        return [str(int(first)), str(int(second))]
    else:
        return [ str( int(stone) * 2024 )]
    
def solve_part1(stones, n_blink):
    for i in range(n_blink):
        new_stones = []
        for stone in stones:
            res = blink(stone)
            for s in res:
                new_stones.append(s)
        #print(f"{i + 1} blink:",new_stones)
        stones = new_stones
    #print(f"After {n_blink}: you got {len(stones)} stones")

def propagate_down(stone, remain, memo):
    #print(f"calling with {stone} remain {remain}")
    if (stone, remain) in memo:
        return memo[(stone, remain)]
    if remain == 1:
        return len(blink(stone))

    else:
        if int(stone) == 0:
            r = propagate_down('1', remain-1, memo)
            memo[(stone, remain)] = r
            return r
        elif len(stone) % 2 == 0:
            first = stone[:len(stone)//2]
            second = stone[len(stone)//2:]
            
            f = propagate_down(str(int(first)), remain-1, memo)
            s = propagate_down(str(int(second)), remain-1, memo)
            memo[(stone, remain)] = f + s
            #print(f" f {f} ({first})  s{s} ({second})")
            return f + s
        else:
            r = propagate_down(str(int(stone) * 2024 ), remain-1, memo)
            memo[(stone, remain)] = r
            return r
def solve_part2(stones, rep):
    memo = {}
    total = 0
    for stone in stones:
        t = propagate_down(stone, rep, memo)
        total += t
    print(f"After rep {rep} ::  {total} stones")

if __name__ == "__main__":
    stones = read_input()
    solve_part1(stones, 25)
    solve_part2(stones, 75)
    #k = propagate_down('999', 4, memo)

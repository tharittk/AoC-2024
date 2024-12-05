
def read_input():
    note1 = []
    note2 = []
    with open("./input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            l = line.strip().split("   ")
            a, b = int(l[0]), int(l[1])

            note1.append(a)
            note2.append(b)
    return note1, note2

def solve_part1(note1, note2):
    note1.sort()
    note2.sort()

    dist_sum = 0
    for i in range(len(note1)):
        dist_sum += abs(note1[i] - note2[i])

    print(f"Total distance {dist_sum}")

def solve_part2(note1, note2):

    # id to frequency table
    id_to_freq = {}
    for idx in note2:
        if idx in id_to_freq:
            id_to_freq[idx] += 1
        else:
            id_to_freq[idx] = 1

    # similarity score
    score = 0
    for idx in note1:
        if idx in id_to_freq:
            score += idx * id_to_freq[idx]

    print(f"Similarity score {score}")


if __name__ == "__main__":
    note1, note2 = read_input()
    
    solve_part1(note1, note2)
    
    solve_part2(note1, note2)    

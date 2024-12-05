# By Tharit T. | Dec 5, 2024

def read_input():
    
    POINTED_BY = {}
    POINT_TO = {}
    updates = []
    
    with open("./input.txt") as f:
        while True:
            line = f.readline()
            
            if line == "\n":
                break
            
            nodes = line.strip().split("|")
            head = int(nodes[0])
            tail = int(nodes[1])

            if not head in POINT_TO:
                POINT_TO[head] = {}
            POINT_TO[head][tail] = ''

            if not tail in POINTED_BY:
                POINTED_BY[tail] = {}
            POINTED_BY[tail][head] = ''
               
        while True:
            line = f.readline()
            if not line:
                break
            tmp = line.strip().split(",")
            update = [int(i) for i in tmp]
            updates.append(update)
            
        return POINTED_BY, POINT_TO, updates

def check_update(POINTED_BY, update):
    
    # page that show up first must not be pointed by what comes after
    # O(n2) when n is number of page in update

    for i in range(len(update)):
        page_front = update[i]
        for j in range(i + 1, len(update)):
            page_after = update[j]

            if page_front in POINTED_BY and page_after in POINTED_BY[page_front]:
                return False
    return True

def solve_part1(POINTED_BY ,updates):
    total = 0
    for update in updates:
        if check_update(POINTED_BY, update):
            mid = len(update) // 2
            total += update[mid]

    print(f"Total sum of mid of incorrect order: {total}")

def fix_incorrect_update(POINT_TO, update):

    # topological sort
    
    visited = [False for i in range(len(update))]
    stack = []

    def dfs(root_idx, update, visited, stack):
        visited[root_idx] = True
        src = update[root_idx]
        for i in range(root_idx, len(update)):
            dest = update[i]
            if src in POINT_TO and dest in POINT_TO[src] and not visited[i]:
                dfs(i, update, visited, stack)
        stack.append(src)

    # There might be more than one Strongly Connected Component (SCC)
    for i in range(len(update)):
        if not visited[i]:
            dfs(i, update, visited, stack)
    
    # Topological sort is the stack read in reverse
    corrected = stack[::-1]

    return corrected

def solve_part2(POINTED_BY, POINT_TO, updates):
    total = 0
    for update in updates:
        if not check_update(POINTED_BY, update):
            # fix
            corrected = fix_incorrect_update(POINT_TO, update)
            mid = len(corrected) // 2
            total += corrected[mid]
            
    print(f"Total sum of mid of corrected order: {total}")



if __name__ == "__main__":
    POINTED_BY, POINT_TO, updates = read_input()
    
    solve_part1(POINTED_BY, updates)

    solve_part2(POINTED_BY, POINT_TO, updates)
  

def read_input():
    out = ""
    with open("./input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            out = line.strip()
    return out

def expand(diskmap):
    is_file_turn = True
    file_id = 0
    full_map = []
    for c in diskmap:
        if is_file_turn:
            for i in range(int(c)):
                full_map.append(str(file_id))
            is_file_turn = False
            file_id += 1
        else:
            for i in range(int(c)):
                full_map.append(".")
            is_file_turn = True
    return full_map

def compact(full_map):
    write_idx = 0
    read_idx = len(full_map) - 1

    while write_idx < read_idx:
        
        # get next write_idx
        while full_map[write_idx] != '.':
            write_idx += 1

        # get next read_idx
        while full_map[read_idx] == '.':
            read_idx -= 1

        if write_idx > read_idx:
            break
        # swap
        full_map[write_idx] = full_map[read_idx]
        full_map[read_idx] = '.'
        
        # next iteration
        write_idx += 1
        read_idx -= 1
    return full_map

def checksum(compact):
    total = 0
    for i, c in enumerate(compact):
        if c == '.':
            continue
        total += i * int(c)
    return total

def solve_part1(diskmap):
    full_map = expand(diskmap)
    compacted = compact(full_map)
    total = checksum(compacted)
    print(f"Checksum: {total}")


class LinkedList:
    def __init__(self, size):
        self.size = size
        self.next = None
        self.files = []

    def allocate_to(self, file):
        self.files.append(file)
        self.size -= file.size
        assert self.size >= 0

class File:
    def __init__(self, idx, size):
        self.id = idx
        self.size = size

def expand_linked_list(head):
    while head:
        print("head size ", head.size, [f.id for f in head.files])
        head = head.next

def expand_files(files):
    for file in files:
        print(file.id, file.size)

def expand_with_free_node(diskmap):
    is_file_turn = True
    file_id = 0
    files = []
    head = None

    for c in diskmap:
        if is_file_turn:
            files.append(File(file_id, int(c)))
            is_file_turn = False
            file_id += 1
        else:
            if not head:
                head = LinkedList(int(c))
                curr = head
            else:
                new_node = LinkedList(int(c))
                curr.next = new_node
                curr = new_node
            is_file_turn = True
    return files, head

def compact_with_free_node(files, head):
    
    # from higest file index
    for i in range(len(files)-1, -1, -1):
        file = files[i]

        # find first free node that fits
        curr = head
        free_node_id = 0
        while curr and curr.size < file.size and free_node_id < file.id:
            curr = curr.next
            free_node_id += 1
        
        # nothing fits to the left
        if (not curr) or free_node_id >= file.id:
            continue
        else:
            curr.allocate_to(file)
            # Set as moved
            files[i] = File(0, files[i].size)
    
    return files, head

def create_full_map_after_compact(files, head):
    # interleaving
    full_map = []
    ifile = 0
    
    while ifile < len(files) or head:
        f = files[ifile]
        
        # those marked as moved
        c = "." if f.id == 0 and ifile != 0 else str(f.id)
        for i in range(f.size):
            full_map.append(c)
        
        if not head:
            break
        for file in head.files:
            for i in range(file.size):
                full_map.append(str(file.id))

        for i in range(head.size):
            full_map.append(".")

        ifile += 1
        head = head.next
    return full_map

def solve_part2(diskmap):
    files, head = expand_with_free_node(diskmap)
    files, head = compact_with_free_node(files, head)
    full_map = create_full_map_after_compact(files, head)
    total = checksum(full_map)

    print(f"Checksum Part2: {total}")

if __name__ == "__main__":
    diskmap = read_input()
    solve_part1(diskmap)
    solve_part2(diskmap)

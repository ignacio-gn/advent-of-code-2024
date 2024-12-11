from util.util import *


def calculate_checksum(disk):
    out = 0
    for i in range(len(disk)):
        if disk[i] == ".":
            continue
        out += disk[i] * i
    return out


def solve_1(disk):
    idx_free = 0
    idx_block = len(disk) - 1
    while idx_free < idx_block:
        while disk[idx_free] != ".":
            idx_free += 1
        while disk[idx_block] == ".":
            idx_block -= 1
        if idx_free < idx_block:
            disk = disk[:idx_free] + [disk[idx_block]] \
                   + disk[idx_free + 1:idx_block] + ["."] + disk[idx_block + 1:]
    return calculate_checksum(disk)


def flatten(list):
    return [x for sublist in list for x in sublist]


def solve_2(line):
    disk = [[(i // 2) if i % 2 == 0 else 0] * int(line[i]) for i in range(len(line))]
    free_spaces = {
        i: int(line[i]) for i in range(1, len(line), 2)
    }

    for i in range(len(disk)-1, -1, -1):
        if i % 2 != 0: continue
        block = disk[i]

        for free_idx, free_block in free_spaces.items():
            if free_idx > i: break
            if len(block) <= free_block:
                disk[free_idx] = disk[free_idx][:len(disk[free_idx])-free_block] + block + disk[free_idx][:free_block - len(block)]
                free_spaces[free_idx] -= len(block)
                disk[i] = [0] * len(block)
                break

    return calculate_checksum(flatten(disk))


if __name__ == "__main__":
    line = read_file("input/09.txt")[0]
    disk = []
    for i, digit in enumerate(line):
        if i % 2 == 0:
            disk += [i // 2 for _ in range(int(digit))]
        else:
            disk += ["." for _ in range(int(digit))]

    print(solve_1(disk))
    print(solve_2(line))

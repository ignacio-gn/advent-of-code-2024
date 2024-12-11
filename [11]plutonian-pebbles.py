from util.util import *

def process_pebble(n):
    n_str = str(n)
    len_n_str = len(n_str)
    if len(n_str) % 2 == 0:
        return [int(n_str[:len_n_str // 2]), int(n_str[len_n_str // 2:])]

    if n != 0:
        return [n * 2024]
    return [1]

def solve_1(lines):
    N_BLINKS = 25
    for i in range(N_BLINKS):
        lines = [item for n in lines for item in process_pebble(n)]

    return len(lines)

def solve_2(lines):
    N_BLINKS = 75
    pebbles = {pebble: lines.count(pebble) for pebble in set(lines)}
    for i in range(N_BLINKS):
        local_pebbles = {}
        for pebble, count in pebbles.items():
            for item in process_pebble(pebble):
                local_pebbles[item] = \
                    count if item not in local_pebbles \
                    else local_pebbles[item] + count
                
        pebbles = local_pebbles

    return sum(pebbles.values())

if __name__ == "__main__":
    lines = list(map(int, read_file("input/11.txt")[0].split(" ")))

    print(solve_1(lines))
    print(solve_2(lines))
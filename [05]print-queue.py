import itertools as it
import math
from functools import cmp_to_key

from util.util import *


def compare(rules, a, b):
    if [a, b] in rules:
        return 1
    elif [b, a] in rules:
        return -1
    return 0

def solve_1(rules, updates):
    return sum([
        line[len(line) // 2]
        for line in filter(
            lambda line: all([
                compare(rules, a, b) >= 0
                for a, b in it.pairwise(line)
            ]),
            updates
        )
    ])

def solve_2(rules, updates):
    sorted_updates = [sorted(update, key=cmp_to_key(lambda a, b: compare(rules, b, a))) for update in updates]
    return sum([
        line[len(line)//2]
        for line in filter(
            lambda update: update not in updates,
            sorted_updates
        )
    ])

if __name__ == "__main__":
    lines = "X".join(read_file("input/05.txt"))
    rules, updates = lines.split("XX")
    rules = [[int(num) for num in rule.split("|")] for rule in rules.split("X")]
    updates = [[int(update) for update in updates.split(",")] for updates in updates.split("X")]

    print(solve_1(rules, updates))
    print(solve_2(rules, updates))
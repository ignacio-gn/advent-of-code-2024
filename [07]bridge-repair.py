import time
from itertools import permutations, product

from util.util import *

OPERATORS = ["+", "*"]


def apply_operator(op, a, b):
    if op == "+":
        return a + b
    elif op == "*":
        return a * b
    elif op == "|":
        return int(f"{a}{b}")


def can_get_result(result, operands):
    for ops in product(OPERATORS, repeat=len(operands) - 1):
        value = operands[0]
        for i, op in enumerate(ops):
            value = apply_operator(op, value, operands[i + 1])
        if value == result:
            return True
    return False


def solve_1(lines):
    output = 0
    for line in lines:
        result, *operands = line
        if can_get_result(result, operands):
            output += result

    return output


def solve_2(lines):
    OPERATORS.append("|")
    return solve_1(lines)


if __name__ == "__main__":
    lines = read_file("input/07.txt")
    lines = [[int(parts[0]), *list(map(int, parts[1:]))] for parts in [line.replace(":", "").split(" ") for line in lines]]

    print(solve_1(lines))
    print(solve_2(lines))
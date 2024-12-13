import re

from util.util import *
import numpy as np


def parse_matrix(lines):
    out_00 = re.match(r"Button A: X\+(\d+),*", lines[0]).group(1)
    out_10 = re.match(r"Button A:.*Y\+(\d+),*", lines[0]).group(1)
    out_01 = re.match(r"Button B: X\+(\d+),*", lines[1]).group(1)
    out_11 = re.match(r"Button B:.*Y\+(\d+),*", lines[1]).group(1)
    return np.array([[int(out_00), int(out_01)],[int(out_10), int(out_11)]])


def parse_prices(lines):
    out_00 = re.match(r"Prize: X=(\d+),*", lines[2]).group(1)
    out_10 = re.match(r"Prize:.*Y=(\d+)", lines[2]).group(1)
    return np.array([int(out_00), int(out_10)])


def solve_1(matrices, prices):
    out = 0
    for i in range(len(matrices)):
        matrix = matrices[i]
        price = prices[i]

        solution = np.linalg.solve(matrix, price)
        x, y = solution[0], solution[1]
        a, b = round(x), round(y)
        if (a-x) ** 2 + (b-y) ** 2 >= 1e-4:
            continue
        else:
            out += a * 3 + b
    return out


def solve_2(matrices, prices):
    return solve_1(matrices, [price + 10000000000000 for price in prices])


if __name__ == "__main__":
    lines = [line.split("\n") for line in "\n".join(read_file("input/13.txt")).split("\n\n")]
    matrices = [parse_matrix(line) for line in lines]
    prices = [parse_prices(line) for line in lines]

    print(solve_1(matrices, prices))
    print(solve_2(matrices, prices))
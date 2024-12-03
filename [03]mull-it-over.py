from util.util import read_file
import re


def solve_1(line):
    return sum([
        int(a) * int(b) for a, b
        in re.findall(
            r"mul\((\d+),(\d+)\)",
            line
        )
    ])


def solve_2(line):
    return sum([
        solve_1(segment.split("don't()")[0]) for segment
        in line.split("do()")
    ])


if __name__ == "__main__":
    line = "".join(read_file("input/03.txt"))

    print(solve_1(line))
    print(solve_2(line))

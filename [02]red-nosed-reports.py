from util.util import read_file
import itertools as it

def solve_1(lines):
    return sum(
        all([
            (b - a) in [1, 2, 3] if line[0] < line[1]
            else (a - b) in [1, 2, 3]
            for a, b in it.pairwise(line)
        ]) for line in lines
    )


def solve_2(lines):
    build_differences_excluding_i = lambda line, i: [
        (line[:i] + line[i+1:])[j+1] - (line[:i] + line[i+1:])[j]
        for j in range(len(line[:i] + line[i+1:]) - 1)
    ]
    return sum([
        any([
            all(map(lambda x: x in [1, 2, 3], build_differences_excluding_i(line, i))) or \
            all(map(lambda x: x in [-1, -2, -3], build_differences_excluding_i(line, i)))
            for i in range(len(line))
        ])
        for line in lines
    ])


if __name__ == "__main__":
    inp = read_file("input/02.txt")
    lines = [list(map(int, line.split(" "))) for line in inp]

    print(solve_1(lines))
    print(solve_2(lines))
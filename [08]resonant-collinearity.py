import itertools

from util.util import *


def calculate_antinode(pos1, pos2):
    """
    y = 2y_2 - y_1
    x = 2x_2 - x_1
    """
    return (
        (2 * pos2[0] - pos1[0]),
        (2 * pos2[1] - pos1[1])
    )


def solve_1(antennas, dimensions):
    antinodes = set()
    for frequency, positions in antennas.items():
        for position in itertools.product(positions, repeat=2):
            a1, a2 = position
            if a1 == a2:
                continue
            antinode = calculate_antinode(a1, a2)
            if 0 <= antinode[0] < dimensions[0] and 0 <= antinode[1] < dimensions[1]:
                antinodes.add(calculate_antinode(a1, a2))

    return len(antinodes)


def generate_antinode(position, antinode):
    i = 0
    while True:
        yield (antinode[0] + i * (antinode[0] - position[0]), antinode[1] + i * (antinode[1] - position[1]))
        i += 1


def solve_2(antennas, dimensions):
    antinodes = set()
    for frequency, positions in antennas.items():
        for position in itertools.product(positions, repeat=2):
            a1, a2 = position
            if a1 == a2:
                continue
            antinode = calculate_antinode(a1, a2)
            for local_antinode in generate_antinode(a2, antinode):
                if 0 <= local_antinode[0] < dimensions[0] and 0 <= local_antinode[1] < dimensions[1]:
                    antinodes.add(local_antinode)
                else:
                    break

    for antenna in antennas.values():
        for position in antenna:
            antinodes.add(position)

    return len(antinodes)


if __name__ == "__main__":
    lines = read_file("input/08.txt")
    antennas: dict[str, list[tuple[int, int]]] = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                if not antennas.get(char):
                    antennas[char] = []
                antennas[char].append((y, x))
    rows, cols = len(lines), len(lines[0])

    print(solve_1(antennas, dimensions=(rows, cols)))
    print(solve_2(antennas, dimensions=(rows, cols)))
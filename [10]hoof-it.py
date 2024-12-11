from util.util import *

class MapGrid(Grid):
    def __init__(self, grid):
        super().__init__(grid)


def solve_1(grid):
    hilltops = Grid([[set() if grid[y][x] != 9 else {(y, x)} for x in range(grid.cols)] for y in range(grid.rows)])

    for i in range(8, -1, -1):
        next_hilltops = Grid([[set() for x in range(grid.cols)] for y in range(grid.rows)])
        for y in range(grid.rows):
            for x in range(grid.cols):
                if grid.get(y, x) == i:
                    adjacent = hilltops.get_adjacent_from_directions(x, y, ["N", "E", "S", "W"])
                    out = set()
                    for item in flatten(adjacent):
                        out |= item

                    next_hilltops[y][x] |= out
        hilltops = next_hilltops

    out = 0
    for line in hilltops:
        for item in line:
            out += len(item)
    return out

def solve_2(grid):
    hilltops = Grid(
        [[0 if grid[y][x] != 9 else 1 for x in range(grid.cols)] for y in
         range(grid.rows)])

    for i in range(8, -1, -1):
        next_hilltops = Grid(
            [[0 for x in range(grid.cols)] for y in range(grid.rows)])
        for y in range(grid.rows):
            for x in range(grid.cols):
                if grid.get(y, x) == i:
                    adjacent = hilltops.get_adjacent_from_directions(x, y, ["N", "E", "S", "W"])
                    out = 0
                    for item in flatten(adjacent):
                        out += item

                    next_hilltops[y][x] += out
        hilltops = next_hilltops

    out = 0
    for line in hilltops:
        for item in line:
            out += item
    return out

if __name__ == "__main__":
    lines = [list(map(int, list(line))) for line in read_file("input/10.txt")]
    grid = Grid(lines)

    print(solve_1(grid))
    print(solve_2(grid))
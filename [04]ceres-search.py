from util.util import read_file, Grid


def solve_1(lines):
    grid = Grid(lines)
    output = 0

    for y in range(grid.rows):
        for x in range(grid.cols):
            if grid.grid[y][x] == "X":
                output += sum(
                    1 for word in grid.get_adjacent_from(x, y, 4)
                    if  "XMAS" == "".join(word)
                )

    return output


def solve_2(lines):
    grid = Grid(lines)
    output = 0

    for y in range(1, grid.rows-1):
        for x in range(1, grid.cols-1):
            if grid.grid[y][x] == "A":
                nw_se = grid.get_next_n_from(x, y, 2, "NW")[1:] + \
                        grid.get_next_n_from(x, y, 2, "SE")[1:]
                ne_sw = grid.get_next_n_from(x, y, 2, "NE")[1:] + \
                        grid.get_next_n_from(x, y, 2, "SW")[1:]
                if {"M", "S"} == set(nw_se) == set(ne_sw):
                    output += 1

    return output


if __name__ == "__main__":
    lines = read_file("input/04.txt")
    test = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split("\n")[1:]

    print(solve_1(lines))
    print(solve_2(lines))
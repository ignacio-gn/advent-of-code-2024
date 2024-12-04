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

"""
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?

"""

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
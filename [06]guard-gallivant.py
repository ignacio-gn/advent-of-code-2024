import time
from copy import copy, deepcopy


from util.util import *


class Guard():
    def __init__(self,grid):
        self.direction = "N"
        self.grid = grid
        self.y = self.__get_guard_start_position()[0]
        self.x = self.__get_guard_start_position()[1]

    def __get_guard_start_position(self):
        for y in range(self.grid.rows):
            for x in range(self.grid.cols):
                if self.grid[y][x] == "^":
                    return y, x

    def move(self):
        next_x = self.x
        next_y = self.y
        if self.direction == "N":
            next_y = self.y - 1
        if self.direction == "E":
            next_x = self.x + 1
        if self.direction == "S":
            next_y = self.y + 1
        if self.direction == "W":
            next_x = self.x - 1

        if self.grid.get(y=next_y, x=next_x) == "#":
            self.direction = self.__turn_right()
        else:
            self.grid[self.y][self.x] += f"X{self.direction}"
            self.y = next_y
            self.x = next_x

    def is_out_of_bounds(self):
        return (self.y < 0
                or self.y >= self.grid.rows
                or self.x < 0
                or self.x >= self.grid.cols)

    def is_in_a_loop(self):
        return self.direction in self.grid.get(self.y, self.x)

    def __turn_right(self):
        return {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }[self.direction]


class MapGrid(Grid):
    def __init__(self, lines):
        super().__init__(lines)
        self.guard = Guard(self)

    def tick(self):
        self.guard.move()

    def get_distinct_positions(self):
        return sum([
            1 for y in range(self.rows)
            for x in range(self.cols)
            if "X" in self[y][x]
        ])


def solve_1(map_grid):
    while not map_grid.guard.is_out_of_bounds():
        map_grid.tick()

    return map_grid.get_distinct_positions()

def solve_2(map_grid):
    output = 0
    for y in range(map_grid.rows):
        print(f"output={output} | y={y} (/{map_grid.rows}) in {time.time() - start}s")
        for x in range(map_grid.cols):
            if map_grid[y][x] in "^#":
                continue

            local_map = deepcopy(map_grid)
            local_map.guard = Guard(local_map)
            local_map[y][x] = "#"

            while not local_map.guard.is_out_of_bounds() and not local_map.guard.is_in_a_loop():
                local_map.tick()

            if not local_map.guard.is_out_of_bounds() \
                and local_map.guard.is_in_a_loop():
                output += 1

    return output

if __name__ == "__main__":
    start = time.time()
    print(solve_1(MapGrid([list(line) for line in read_file("input/06.txt")])))
    print(solve_2(MapGrid([list(line) for line in read_file("input/06.txt")])))
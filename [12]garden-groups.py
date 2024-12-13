from util.util import *

class Plot:
    def __init__(self, char, grid, coords=[]):
        self.char = char
        self.perimeter = 0
        self.area = 0
        self.coords = coords
        self.grid: Gridv2= grid
        self.sides = 0

    def generate_coords(self):
        visited = set(self.coords)
        queue = set(self.grid.get_adjacent_from(self.coords[0][0], self.coords[0][1], idx=True))
        while queue:
            coord = queue.pop()
            if coord in visited:
                continue
            visited.add(coord)
            tile = self.grid.get(coord[0], coord[1])
            if tile == self.char:
                self.coords.append(coord)
                queue.update(self.grid.get_adjacent_from(coord[0], coord[1], idx=True))

    def calculate_area(self):
        return len(self.coords)

    def calculate_perimeter(self):
        return len(list(filter(
            lambda coord: grid.get(coord[0], coord[1]) != self.char,
            flatten(grid.get_adjacent_from(tile[0], tile[1], idx=True) for tile in self.coords)
        ))) + sum([4 - len(grid.get_adjacent_from(tile[0], tile[1])) for tile in self.coords])

    def calculate(self):
        self.area = self.calculate_area()
        self.perimeter = self.calculate_perimeter()
        self.sides = self.calculate_n_sides()

    def get_price(self, discount=False):
        self.calculate()
        return self.area * self.perimeter if not discount else self.area * self.sides

    def calculate_n_sides(self):
        out = 0
        for coord in self.coords:
            # outer corners
            # |‾
            out += (coord[0], coord[1] - 1) not in self.coords and (coord[0] - 1, coord[1]) not in self.coords
            # ‾|
            out += (coord[0], coord[1] + 1) not in self.coords and (coord[0] - 1, coord[1]) not in self.coords
            # |_
            out += (coord[0], coord[1] - 1) not in self.coords and (coord[0] + 1, coord[1]) not in self.coords
            # _|
            out += (coord[0], coord[1] + 1) not in self.coords and (coord[0] + 1, coord[1]) not in self.coords

            # inner corners
            # _|
            out += (coord[0], coord[1] - 1) in self.coords and (coord[0] - 1, coord[1]) in self.coords and not (coord[0] - 1, coord[1] - 1) in self.coords
            # |_
            out += (coord[0], coord[1] + 1) in self.coords and (coord[0] - 1, coord[1]) in self.coords and not (coord[0] - 1, coord[1] + 1) in self.coords
            # ‾|
            out += (coord[0], coord[1] - 1) in self.coords and (coord[0] + 1, coord[1]) in self.coords and not (coord[0] + 1, coord[1] - 1) in self.coords
            # |‾
            out += (coord[0], coord[1] + 1) in self.coords and (coord[0] + 1, coord[1]) in self.coords and not (coord[0] + 1, coord[1] + 1) in self.coords

        self.sides = out
        return out

    def __str__(self):
        return f"Plot {self.char} with {len(self.coords)} coords"

    def __repr__(self):
        return str(self)


def solve_1(plots):
    return sum([plot.get_price() for plot in plots])

def solve_2(plots):
    return sum([plot.get_price(discount=True) for plot in plots])

if __name__ == "__main__":
    lines = [list(line) for line in read_file("input/12.txt")]
    grid = Gridv2(lines)
    plots = []
    for coord in grid.get_coords():
        tile = grid.get(coord[0], coord[1])
        if any([coord in plot.coords for plot in plots]):
            continue
        plot = Plot(tile, grid=grid, coords=[coord])
        plots.append(plot)
        plot.generate_coords()

    print(solve_1(plots))
    print(solve_2(plots))
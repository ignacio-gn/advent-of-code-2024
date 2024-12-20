import pprint
import functools


class Gridv2:
    def __init__(self, lines):
        self.grid = lines
        self.rows = len(lines)
        self.cols = len(lines[0])
        self.ALL_DIRECTIONS = ["N", "E", "S", "W", "NE", "SE", "SW", "NW"]

    def get(self, y, x):
        return self.grid[y][x] if 0 <= y < self.rows and 0 <= x < self.cols else None

    def get_adjacent_from(self, y, x, directions=["N", "E", "S", "W"], length=1, idx=False):
        result = []
        for i in range(1, length + 1):
            for direction in directions:
                match direction:
                    case "N":
                        ny, nx = y - i, x
                    case "S":
                        ny, nx = y + i, x
                    case "E":
                        ny, nx = y, x + i
                    case "W":
                        ny, nx = y, x - i
                    case "NE":
                        ny, nx = y - i, x + i
                    case "SE":
                        ny, nx = y + i, x + i
                    case "SW":
                        ny, nx = y + i, x - i
                    case "NW":
                        ny, nx = y - i, x - i
                    case _:
                        raise ValueError(
                            "direction must be one of N, S, E, W, NE, SE, SW, NW")

                if 0 <= ny < self.rows and 0 <= nx < self.cols:
                    result.append(self.grid[ny][nx] if not idx else (ny, nx))
        return result

    def get_tiles(self):
        return flatten(self.grid)

    def get_coords(self):
        return [(y, x) for y in range(self.rows) for x in range(self.cols)]

    def __getitem__(self, item):
        return self.grid[item]

    def __setitem__(self, key, value):
        self.grid[key] = value

    def __repr__(self):
        return pprint.pformat(self.grid)

    def __str__(self):
        return pprint.pformat(self.grid)


class Grid:
    def __init__(self, lines):
        self.grid = lines
        self.rows = len(lines)
        self.cols = len(lines[0])

    def get(self, y, x):
        return self.grid[y][x] if 0 <= y < self.rows and 0 <= x < self.cols else None

    def get_adjacent_from(self, x, y, length):
        return [
            self.get_next_n_from(x, y, length, direction)
            for direction in ["N", "E", "S", "W", "NE", "SE", "SW", "NW"]
        ]

    def get_adjacent_from_directions(self, x, y, directions):
        return [
            self.get_next_n_from(x, y, 2, direction)[1:]
            for direction in directions
        ]

    def get_adjacent_idx_from_directions(self, x, y, directions):
        def get_adjacent_idx(x, y, direction):
            match direction:
                case "N":
                    return y - 1, x
                case "S":
                    return y + 1, x
                case "E":
                    return y, x + 1
                case "W":
                    return y, x - 1
                case "NE":
                    return y - 1, x + 1
                case "SE":
                    return y + 1, x + 1
                case "SW":
                    return y + 1, x - 1
                case "NW":
                    return y - 1, x - 1
                case _:
                    raise ValueError("direction must be one of N, S, E, W, NE, SE, SW, NW")
        return list(filter(
            lambda coords: 0 <= coords[0] < self.rows and 0 <= coords[1] < self.cols,
            [get_adjacent_idx(x, y, direction) for direction in directions]
        ))

    def get_next_n_from(self, x, y, length, direction):
        result = []
        for i in range(length):
            match direction:
                case "N":
                    ny, nx = y - i, x
                case "S":
                    ny, nx = y + i, x
                case "E":
                    ny, nx = y, x + i
                case "W":
                    ny, nx = y, x - i
                case "NE":
                    ny, nx = y - i, x + i
                case "SE":
                    ny, nx = y + i, x + i
                case "SW":
                    ny, nx = y + i, x - i
                case "NW":
                    ny, nx = y - i, x - i
                case _:
                    raise ValueError("direction must be one of N, S, E, W, NE, SE, SW, NW")

            if 0 <= ny < self.rows and 0 <= nx < self.cols:
                result.append(self.grid[ny][nx])
            else:
                break
        return result

    def __getitem__(self, item):
        return self.grid[item]

    def __setitem__(self, key, value):
        self.grid[key] = value


def read_file(filename: str) -> list[str]:
    output = list()
    with open(filename) as file:
        for line in file:
            output.append(line.strip())
    return output


def flatten(l):
    return [item for sublist in l for item in sublist]


def flatten_rec(l):
    out = []
    for item in l:
        if isinstance(item, list) or isinstance(item, tuple):
            out += flatten_rec(item)
        else:
            out.append(item)
    return out

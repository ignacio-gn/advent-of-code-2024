import pprint
import functools


class Grid:
    def __init__(self, lines):
        self.grid = lines
        self.rows = len(lines)
        self.cols = len(lines[0])

    def get_adjacent_from(self, x, y, length):
        return [
            self.get_next_n_from(x, y, length, direction)
            for direction in ["N", "E", "S", "W", "NE", "SE", "SW", "NW"]
        ]

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


def read_file(filename: str) -> list[str]:
    output = list()
    with open(filename) as file:
        for line in file:
            output.append(line.strip())
    return output



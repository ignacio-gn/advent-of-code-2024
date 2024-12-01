import pprint
import functools


def read_file(filename: str) -> list[str]:
    output = list()
    with open(filename) as file:
        for line in file:
            output.append(line.strip())
    return output


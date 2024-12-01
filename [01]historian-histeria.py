from util.util import *


def solve_1(list1: list[int], list2: list[int]) -> int:
    return sum([abs(a - b) for a, b in zip(list1, list2)])


def solve_2(list1: list[int], list2: list[int]) -> int:
    return sum([a * list2.count(a) for a in list1])


if __name__ == "__main__":
    inp = read_file("input/01.txt")
    list_1 = sorted(list(map(lambda x: int(x.split(" ")[0]), inp)))
    list_2 = sorted(list(map(lambda x: int(x.split(" ")[-1]), inp)))
    print(solve_1(list_1, list_2))
    print(solve_2(list_1, list_2))
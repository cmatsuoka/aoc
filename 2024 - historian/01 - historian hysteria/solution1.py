import fileinput
from itertools import starmap


def solve(input_file: fileinput.FileInput[str]) -> int:
    list1: list[int] = []
    list2: list[int] = []

    for line in input_file:
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))

    zlist = zip(sorted(list1), sorted(list2))
    return sum(starmap(lambda a, b: abs(a - b), zlist))


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

import fileinput
from typing import List

from number import Number


def solve(input_file):
    n = Number.parse(input_file.readline().strip())
    for line in input_file:
        n += Number.parse(line.strip())
        n.reduce()
    return n.magnitude


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

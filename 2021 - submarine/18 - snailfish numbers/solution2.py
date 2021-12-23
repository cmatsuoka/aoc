import fileinput
from typing import List

from number import Number


def solve(input_file):
    numbers = []
    for line in input_file:
        n = Number.parse(line.strip())
        numbers.append(n)

    max_mag = 0

    lnum = len(numbers)

    for i in range(lnum - 1):
        for j in range(i + 1, lnum):
            a = numbers[i] + numbers[j]
            mag = a.magnitude
            if mag > max_mag:
                max_mag = mag

            a = numbers[j] + numbers[i]
            mag = a.magnitude
            if mag > max_mag:
                max_mag = mag

    return max_mag


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

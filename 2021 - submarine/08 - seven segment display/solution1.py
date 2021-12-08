import fileinput
import re


def solve(input_file):
    count = 0
    for line in input_file:
        parts = line.split(" | ")
        codes = parts[1].split()
        for code in codes:
            size = len(code)
            # number of segments in digits 1, 4, 7, 8
            if size == 2 or size == 4 or size == 3 or size == 7:
                count += 1

    return count


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

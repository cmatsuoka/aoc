import fileinput
import re


def solve(input_file: fileinput.FileInput[str]) -> int:
    data = "%".join(list(input_file))

    total = 0
    for x, y in re.findall(r"mul\((\d+),(\d+)\)", data):
        total += int(x) * int(y)

    return total


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

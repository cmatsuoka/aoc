import fileinput

from common import SectionRange


def solve(input_file):
    total = 0

    for line in input_file:
        range1, range2 = line.split(",")
        sr1 = SectionRange.parse(range1)
        sr2 = SectionRange.parse(range2)

        if sr1.contains(sr2) or sr2.contains(sr1):
            total += 1

    return total


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

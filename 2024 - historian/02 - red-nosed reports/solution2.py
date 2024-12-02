import fileinput
from solution1 import is_safe


def solve(input_file: fileinput.FileInput[str]) -> int:
    safe = 0
    for line in input_file:
        report = list(map(int, line.split()))
        if is_safe(report):
            safe += 1
            continue

        # use dampener
        for i in range(len(report)):
            r = report[:]
            del r[i]
            if is_safe(r):
                safe += 1
                break
            else:
                continue
            break

    return safe


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

import fileinput


def is_safe(report: list[int]) -> bool:
    prev = report[0]
    trend = prev - report[1]

    for entry in report[1:]:
        delta = prev - entry
        if (trend > 0 and delta < 0) or (trend < 0 and delta > 0):
            return False
        d = abs(delta)
        if d < 1 or d > 3:
            return False
        prev = entry

    return True


def solve(input_file: fileinput.FileInput[str]) -> int:
    safe = 0
    for line in input_file:
        report = list(map(int, line.split()))
        if is_safe(report):
            safe += 1

    return safe


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

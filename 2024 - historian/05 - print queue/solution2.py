import fileinput
from functools import cmp_to_key


def solve(input_file: fileinput.FileInput[str]) -> int:
    rules: list[tuple[int, ...]] = []

    def use_rules(a: int, b: int):
        for p0, p1 in rules:
            if a == p0 and b == p1:
                return -1
            if a == p1 and b == p0:
                return 1
        return 0

    for line in input_file:
        line = line.strip()
        if line == "":
            break
        rules.append(tuple([int(x) for x in line.split("|")]))

    sum = 0
    for line in input_file:
        line = line.strip()
        pages = [int(x) for x in line.split(",")]
        for i, p in enumerate(pages):
            before = pages[:i]
            after = pages[i + 1 :]
            for p0, p1 in rules:
                if p0 == p:
                    if p1 in before:
                        break
                elif p1 == p:
                    if p0 in after:
                        break
            else:
                continue
            fixed_pages = sorted(pages, key=cmp_to_key(use_rules))
            sum += fixed_pages[len(fixed_pages) // 2]
            break

    return sum


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

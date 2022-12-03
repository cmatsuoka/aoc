import fileinput


def _priority(char: str) -> int:
    if char <= "Z":
        return ord(char) - ord("A") + 27

    return ord(char) - ord("a") + 1


def solve(input_file):
    total = 0

    for line in input_file:
        content = line.strip()
        size = len(content) // 2
        comp1 = set(content[:size])
        comp2 = set(content[size:])
        total += sum(_priority(x) for x in comp1.intersection(comp2))

    return total


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

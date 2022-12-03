import fileinput


def _priority(char: str) -> int:
    if char <= "Z":
        return ord(char) - ord("A") + 27

    return ord(char) - ord("a") + 1


def solve(input_file):
    total = 0

    for line in input_file:
        elf1 = set(line.strip())
        elf2 = set(input_file.readline().strip())
        elf3 = set(input_file.readline().strip())

        # The badge is the only item type carried by all three Elves
        (badge,) = elf1.intersection(elf2).intersection(elf3)
        total += _priority(badge)

    return total


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

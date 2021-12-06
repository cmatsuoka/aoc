import fileinput


def solve(input_file):
    entries = set()
    for line in input_file:
        entries.add(int(line))

    while True:
        x = entries.pop()
        complement = 2020 - x
        if complement in entries:
            return x * complement


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

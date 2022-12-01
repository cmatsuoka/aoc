import fileinput


def solve(input_file):
    cals = []
    accum = 0

    for line in input_file:
        line = line.strip()
        if not line:
            cals.append(accum)
            accum = 0
            continue

        accum += int(line)

    cals.append(accum)

    return sum(sorted(cals, reverse=True)[:3])


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

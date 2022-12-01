import fileinput


def solve(input_file):
    max_cals = 0
    accum = 0

    for line in input_file:
        line = line.strip()
        if not line:
            if accum > max_cals:
                max_cals = accum

            accum = 0
            continue

        accum += int(line)

    if accum > max_cals:
        max_cals = accum

    return max_cals


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

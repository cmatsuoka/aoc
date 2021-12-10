import fileinput


def solve(input_file):
    entries = [int(x) for x in input_file]
    entries.sort()

    # only one combination at the start
    combinations = {
        0: 1,
    }

    # for each new adapter we add the number of combinations from the
    # possible previous adapters in the chain (rated -3, -2, -1)
    #
    # (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
    #
    # (0)  -> combi(0) = 1
    # (0), 1  -> combi(1) = combi(1 - 1) = 1
    # (0), 1, 4  -> combi(4) = combi(4 - 3) = 1
    # (0), 1, 4, 5  -> combi(5) = combi(5 - 1) = 1
    # (0), 1, 4, 5, 6  -> combi(6) = combi(6 - 2) + combi(6 - 1) = 2
    # (0), 1, 4, 5, 6, 7  -> combi(7) = combi(4) + combi(5) + combi(6) = 4
    # (0), 1, 4, 5, 6, 7, 10  -> combi(10) = combi(7) = 4
    # ...

    for adapter in entries:
        total = 0

        if adapter - 3 in combinations:
            total += combinations[adapter - 3]

        if adapter - 2 in combinations:
            total += combinations[adapter - 2]

        if adapter - 1 in combinations:
            total += combinations[adapter - 1]

        combinations[adapter] = total

    return combinations[entries[-1]]


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

import fileinput


def solve(input_file):
    entries = [int(x) for x in input_file]
    entries.sort()

    jolts = 0
    diff1 = diff2 = diff3 = 0

    for adapter in entries:
        delta = adapter - jolts
        if delta > 3:
            raise RuntimeError("no suitable adapter found")

        if delta == 1:
            diff1 += 1
        elif delta == 2:
            diff2 += 1
        elif delta == 3:
            diff3 += 1
        else:
            raise RuntimeError("diff > 3")

        jolts = adapter

    # device built-in adapter is 3 higher than last adapter
    return diff1 * (diff3 + 1)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

import fileinput
import math


def solve(input_file):
    line = input_file.readline()
    size = len(line.strip())

    # slurp our input data to a list
    val = int(line, 2)
    values = [val] + [int(line, 2) for line in input_file]

    # compute values
    oxygen = _filter(values, size, lambda x, y: x >= y)
    scrubber = _filter(values, size, lambda x, y: x < y)

    return oxygen * scrubber


def _bit_frequency(values, pos):
    freq = 0
    for val in values:
        if val & (0x01 << pos):
            freq += 1

    return freq


def _filter(values, size, condition):
    count = len(values)
    for i in range(size - 1, -1, -1):
        threshold = int(math.ceil(count / 2))
        freq_count = _bit_frequency(values, i)

        if condition(freq_count, threshold):
            values = [v for v in values if v & (0x1 << i)]
        else:
            values = [v for v in values if not (v & (0x1 << i))]

        count = len(values)
        if count == 1:
            break

    if count != 1:
        raise RuntimeError(f"ended with {count} values")

    return values[0]


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

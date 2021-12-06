import fileinput


# obtain the word size and initialize histogram


class Histogram:
    def __init__(self, size):
        self._size = size
        self._data = [0] * size

    def fill(self, line):
        val = int(line, 2)
        for i in range(self._size):
            if val & 0x01:
                self._data[i] += 1
            val >>= 1

    def value(self, i):
        return self._data[i]


def solve(input_file):
    # read input and fill histogram
    line = input_file.readline()
    size = len(line.strip())

    histogram = Histogram(size)

    histogram.fill(line)
    count = 1

    for line in input_file:
        histogram.fill(line)
        count += 1

    # verify most frequent bits

    gamma = 0
    threshold = int(count / 2)
    for i in range(size):
        one_count = histogram.value(i)

        if one_count == threshold:
            raise RuntimeError("same amount of 0s and 1s")

        if one_count > threshold:
            gamma |= 0x01 << i

    epsilon = gamma ^ ((0x01 << size) - 1)

    return gamma * epsilon


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

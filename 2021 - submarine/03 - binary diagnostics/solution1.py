import fileinput


# obtain the word size and initialize histogram

data = fileinput.input()
line = next(data)
size = len(line.strip())

histogram = [0] * size


def fill_histogram(line):
    val = int(line, 2)

    # fill bit frequency histogram
    for i in range(size):
        if val & 0x01:
            histogram[i] += 1
        val >>= 1


# read input and fill histogram

fill_histogram(line)
count = 1

for line in data:
    fill_histogram(line)
    count += 1

# verify most frequent bits

gamma = 0
threshold = int(count / 2)
for i in range(size):
    one_count = histogram[i]

    if one_count == threshold:
        raise RuntimeError("same amount of 0s and 1s")

    if one_count > threshold:
        gamma |= (0x01 << i)

epsilon = gamma ^ ((0x01 << size) - 1)

print(gamma * epsilon)

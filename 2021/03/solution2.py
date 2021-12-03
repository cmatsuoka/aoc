import fileinput
import math

def compute_histogram(values, size):
    histogram = [0] * size
    for val in values:
        for i in range(size):
            if val & 0x01:
                histogram[i] += 1
            val >>= 1
    return histogram

def filter(values, size, condition):
    count = len(values)
    for i in range(size - 1, -1, -1):
        histogram = compute_histogram(values, size)
        threshold = int(math.ceil(count / 2))

        freq_count = histogram[i]
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


# obtain the word size

data = fileinput.input()
line = next(data)
size = len(line.strip())

# slurp our input data to a list
val = int(line, 2)
values = [val]

for line in data:
    val = int(line, 2)
    values.append(val)
    
# compute values

oxygen = filter(values, size, lambda x, y: x >= y)
scrubber = filter(values, size, lambda x, y: x < y)

print(oxygen * scrubber)

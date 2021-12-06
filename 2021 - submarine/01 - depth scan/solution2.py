import fileinput


def solve(input_file):
    aa = int(input_file.readline())
    d0 = int(input_file.readline())
    d1 = int(input_file.readline())

    prev = aa + d0 + d1
    incs = 0

    for line in input_file:
        d2 = int(line)
        curr = d0 + d1 + d2
        if curr > prev:
            incs += 1
        d0 = d1
        d1 = d2
        prev = curr

    return incs


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

import fileinput


def solve(input_file):
    prev = input_file.readline()
    incs = 0

    for curr in input_file:
        if int(curr) > int(prev):
            incs += 1
        prev = curr

    return incs


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

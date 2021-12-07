import fileinput
import argparse

import solution1


def solve(input_file, invalid_value):
    stream = [int(x) for x in input_file]

    for start in range(len(stream)):
        total = 0
        smallest = invalid_value
        largest = 0

        for i in range(start, len(stream)):
            num = stream[i]

            if num > largest:
                largest = num
            if num < smallest:
                smallest = num

            total += stream[i]
            if total == invalid_value:
                return smallest + largest
            if total > invalid_value:
                break

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", dest="invalid_value", type=int)
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()

    files = args.files if len(args.files) > 0 else ("-",)

    print(solve(fileinput.FileInput(files), args.invalid_value))

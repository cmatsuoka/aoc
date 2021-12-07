import fileinput
import argparse


def solve(input_file, preamble_size):
    stream = []

    for i in range(preamble_size):
        stream.append(int(input_file.readline()))

    for line in input_file:
        val = int(line)
        if not _is_valid(val, stream):
            return val

        stream = stream[1:] + [val]

    return None


def _is_valid(val, stream):
    for i in stream:
        complement = val - i
        if complement in stream:
            return True

    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", default="25", dest="preamble_size", type=int)
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()

    files = args.files if len(args.files) > 0 else ("-",)

    print(solve(fileinput.FileInput(files), args.preamble_size))

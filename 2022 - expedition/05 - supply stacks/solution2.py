import fileinput

from common import Cargo


def solve(input_file):
    cargo = Cargo()
    cargo.parse(input_file)
    assert input_file.readline() == "\n"

    for line in input_file:
        (_, num, _, src, _, dest) = line.split(" ")
        cargo.move(int(num), int(src), int(dest), multiple=True)

    return cargo.top_crates()


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

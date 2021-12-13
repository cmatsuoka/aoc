import fileinput
from origami import Origami


def solve(input_file):
    origami = Origami.from_file(input_file)
    origami.fold()
    return origami.count_dots()


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

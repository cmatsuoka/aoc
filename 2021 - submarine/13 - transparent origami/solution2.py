import fileinput
from origami import Origami


def solve(input_file):
    origami = Origami.from_file(input_file)
    while origami.fold():
        pass

    return origami.content()


if __name__ == "__main__":
    for line in solve(fileinput.FileInput()):
        print(line)

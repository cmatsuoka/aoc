import fileinput
from polymerizer import Polymerizer


def solve(input_file, num):
    p = Polymerizer.from_file(input_file)

    for i in range(num):
        p.run()

    min_elem, max_elem = p.get_element_count()

    return max_elem - min_elem


if __name__ == "__main__":
    print(solve(fileinput.FileInput(), 40))

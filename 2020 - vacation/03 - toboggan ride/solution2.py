import fileinput

from mapping import Map


def solve(input_file):
    m = Map.from_file(input_file)
    total = 1

    for args in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        trees = 0
        m.home()

        m.walk(*args)
        while m.is_inside():
            if m.tree_here():
                trees += 1
            m.walk(*args)

        total *= trees

    return total


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

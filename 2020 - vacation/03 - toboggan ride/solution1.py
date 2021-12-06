import fileinput

from mapping import Map


def solve(input_file):
    m = Map.from_file(input_file)

    trees = 0
    m.walk(3, 1)
    while m.is_inside():
        if m.tree_here():
            trees += 1
        m.walk(3, 1)

    return trees


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

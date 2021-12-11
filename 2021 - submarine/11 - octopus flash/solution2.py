import fileinput
from grid import Grid


def solve(input_file, cycles):
    grid = Grid.from_file(input_file)

    for i in range(cycles):
        grid.do_cycle()
        if grid.all_flashed:
            return i + 1

    raise RuntimeError("sorry, never happened")


if __name__ == "__main__":
    print(solve(fileinput.FileInput(), 1000))

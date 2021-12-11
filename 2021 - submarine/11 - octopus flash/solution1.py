import fileinput
from grid import Grid


def solve(input_file, cycles):
    grid = Grid.from_file(input_file)

    for _ in range(cycles):
        grid.do_cycle()

    return grid.flashes


if __name__ == "__main__":
    print(solve(fileinput.FileInput(), 100))

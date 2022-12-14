import fileinput
from typing import List

from common import Point, plot


def _simulate(field: List[List[str]], threshold: int) -> int:
    total = 0
    full = False

    while not full:
        sand = Point(500, 0)

        while not full:
            if sand.y > threshold:
                full = True

            if field[sand.y + 1][sand.x] == ".":
                sand.y += 1
                continue

            if field[sand.y + 1][sand.x - 1] == ".":
                sand.y += 1
                sand.x -= 1
                continue

            if field[sand.y + 1][sand.x + 1] == ".":
                sand.y += 1
                sand.x += 1
                continue

            field[sand.y][sand.x] = "o"
            total += 1
            break

    return total


def solve(input_file: fileinput.FileInput) -> int:
    threshold = 0
    # this would be better with ints but we can optimize later
    field = [["."] * 1000 for _ in range(172)]

    for line in input_file:
        coords = [Point.unmarshal(x) for x in line.split(" -> ")]
        max_y = max([p.y for p in coords])
        if max_y > threshold:
            threshold = max_y
        plot(coords, field)

    return _simulate(field, threshold)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

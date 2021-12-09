import fileinput
from heightmap import HeightMap
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])


def solve(input_file):
    hm = HeightMap.from_file(input_file)
    lowpoints = []

    for y in range(hm.height):
        for x in range(hm.width):
            if hm.is_lowpoint(x, y):
                lowpoints.append(Point(x, y))

    basin_sizes = []
    for point in lowpoints:
        size = hm.flood(point.x, point.y)
        basin_sizes.append(size)

    basin_sizes.sort(reverse=True)

    total = 1
    for size in basin_sizes[:3]:
        total *= size

    return total


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

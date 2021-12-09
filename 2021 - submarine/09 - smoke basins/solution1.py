import fileinput
from heightmap import HeightMap


def solve(input_file):
    hm = HeightMap.from_file(input_file)
    risk = 0

    for y in range(hm.height):
        for x in range(hm.width):
            if hm.is_lowpoint(x, y):
                risk += 1 + hm.value(x, y)

    return risk


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

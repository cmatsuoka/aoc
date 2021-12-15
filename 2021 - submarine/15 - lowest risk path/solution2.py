import fileinput
from mapping import RiskMap


def solve(input_file):
    data = []
    for line in input_file:
        data.append([int(x) for x in list(line.strip())])

    r = RiskMap(_unfold_map(data))
    return r.dijkstra()


def _unfold_map(data):
    width = len(data[0])
    height = len(data)

    new_map = [[0] * width * 5 for _ in range(height * 5)]
    for i in range(5):
        for j in range(5):
            offset = i + j
            for y in range(height):
                for x in range(width):
                    val = data[y][x] + offset
                    if val > 9:
                        val -= 9
                    new_map[i * height + y][j * width + x] = val
    return new_map


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

import fileinput
from mapping import RiskMap


def solve(input_file):
    r = RiskMap.from_file(input_file)
    return r.dijkstra()


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

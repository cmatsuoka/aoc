import fileinput
from typing import Any, Generator


class Island:
    def __init__(self, data: list[list[int]]) -> None:
        self._data = data
        self._w = len(data[0])
        self._h = len(data)
        self.score = 0

    def find_trailhead(self) -> Generator[tuple[int, int], Any, Any]:
        for y in range(self._h):
            for x in range(self._w):
                if self._data[y][x] == 0:
                    yield x, y

    def reset(self):  # this is an ugly hack
        for y in range(self._h):
            for x in range(self._w):
                if self._data[y][x] == 900:
                    self._data[y][x] = 9

    def traverse(self, prev: int, x: int, y: int):
        height = self._data[y][x]

        if height - prev != 1:
            return

        if height == 9:
            self._data[y][x] = 900  # mark destination as already reached
            self.score += 1
            return

        if x > 0:
            self.traverse(height, x - 1, y)
        if y > 0:
            self.traverse(height, x, y - 1)
        if x < (self._w - 1):
            self.traverse(height, x + 1, y)
        if y < (self._h - 1):
            self.traverse(height, x, y + 1)


def solve(input_file: fileinput.FileInput[str]) -> int:
    data = [[int(x) for x in line.strip()] for line in input_file]

    island = Island(data)
    for head in island.find_trailhead():
        island.reset()
        island.traverse(-1, *head)

    return island.score


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

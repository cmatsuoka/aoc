import fileinput
from typing import List


class DirectionMap:
    def __init__(self, w: int, h: int) -> None:
        self._map = [([False] * w) for _ in range(h)]
        self._width = w
        self._height = w

    def view_from_left(self, height_map: List[str]) -> None:
        y = 0
        while y < self._height:
            self._map[y][0] = True
            ref = height_map[y][0]
            x = 1
            while x < self._width:
                current = height_map[y][x]
                if current > ref:
                    self._map[y][x] = True
                    ref = current
                x += 1
            y += 1

    def view_from_right(self, height_map: List[str]) -> None:
        y = 0
        while y < self._height:
            self._map[y][self._width - 1] = True
            ref = height_map[y][self._width - 1]
            x = self._width - 2
            while x >= 0:
                current = height_map[y][x]
                if current > ref:
                    self._map[y][x] = True
                    ref = current
                x -= 1
            y += 1

    def view_from_top(self, height_map: List[str]) -> None:
        x = 0
        while x < self._width:
            self._map[0][x] = True
            ref = height_map[0][x]
            y = 1
            while y < self._height:
                current = height_map[y][x]
                if current > ref:
                    self._map[y][x] = True
                    ref = current
                y += 1
            x += 1

    def view_from_bottom(self, height_map: List[str]) -> None:
        x = 0
        while x < self._width:
            self._map[self._height - 1][x] = True
            ref = height_map[self._height - 1][x]
            y = self._height - 2
            while y >= 0:
                current = height_map[y][x]
                if current > ref:
                    self._map[y][x] = True
                    ref = current
                y -= 1
            x += 1

    def count_visible(self) -> int:
        total = 0
        for y in range(self._height):
            for x in range(self._width):
                if self._map[y][x]:
                    total += 1

        return total


def solve(input_file):
    height_map = [line.strip() for line in input_file]
    w = len(height_map[0])
    h = len(height_map)

    dirmap = DirectionMap(w, h)

    dirmap.view_from_left(height_map)
    dirmap.view_from_right(height_map)
    dirmap.view_from_top(height_map)
    dirmap.view_from_bottom(height_map)

    return dirmap.count_visible()


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

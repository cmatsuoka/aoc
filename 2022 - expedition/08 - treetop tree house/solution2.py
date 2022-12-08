import fileinput
from typing import List


class ScenicMap:
    def __init__(self, data: List[List[int]]) -> None:
        self._data = data
        self._width = len(data[0])
        self._height = len(data)

    def scan(self) -> int:
        max_score = 0

        for y in range(self._height):
            for x in range(self._width):
                score = self._get_score(x, y)
                if score > max_score:
                    max_score = score

        return max_score

    def _get_score(self, x: int, y: int) -> int:
        score_up = self._scenic_score(x, y, 0, -1)
        score_down = self._scenic_score(x, y, 0, 1)
        score_left = self._scenic_score(x, y, -1, 0)
        score_right = self._scenic_score(x, y, 1, 0)

        return score_up * score_down * score_left * score_right

    def _scenic_score(self, x: int, y: int, dx: int, dy: int):
        score = 0
        current = self._data[y][x]
        x += dx
        y += dy
        while x >= 0 and x < self._width and y >= 0 and y < self._height:
            score += 1
            if self._data[y][x] >= current:
                break
            x += dx
            y += dy
        return score


def solve(input_file):
    height_map = [line.strip() for line in input_file]
    scenic_map = ScenicMap(height_map)

    return scenic_map.scan()


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

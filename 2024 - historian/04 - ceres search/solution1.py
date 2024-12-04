import fileinput


class Board:
    def __init__(self, data: list[str]) -> None:
        self._data = data
        self._w = len(data[0])
        self._h = len(data)
        self._buffer = "...."
        self._words: list[str]

    def scan(self, word: str) -> int:
        self._words = [word, word[::-1]]
        return self._scan_h() + self._scan_v() + self._scan_d1() + self._scan_d2()

    def _clean(self) -> None:
        self._buffer = "...."

    def _slurp_and_check(self, x: int, y: int) -> bool:
        self._buffer = self._buffer[1:] + self._data[y][x]
        return self._buffer in self._words

    def _scan_h(self) -> int:
        count = 0
        for y in range(self._h):
            self._clean()
            for x in range(self._w):
                if self._slurp_and_check(x, y):
                    count += 1
        return count

    def _scan_v(self) -> int:
        count = 0
        for x in range(self._w):
            self._clean()
            for y in range(self._h):
                if self._slurp_and_check(x, y):
                    count += 1
        return count

    def _scan_d1(self) -> int:
        count = 0
        for m in range(-self._h, self._w - 4 + 1):
            self._clean()
            for y in range(self._h):
                x = m + y
                if x < 0:  # not at left border yet
                    continue
                if x >= self._w:  # beyond right border
                    break
                if self._slurp_and_check(x, y):
                    count += 1
        return count

    def _scan_d2(self) -> int:
        count = 0
        for m in range(4, self._w + self._h):
            self._clean()
            for y in range(self._h):
                x = m - y
                if x >= self._w:  # not at right border yet
                    continue
                if x < 0:  # beyond left border
                    break
                if self._slurp_and_check(x, y):
                    count += 1
        return count


def solve(input_file: fileinput.FileInput[str]) -> int:
    board = Board([line.strip() for line in input_file])
    return board.scan("XMAS")


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

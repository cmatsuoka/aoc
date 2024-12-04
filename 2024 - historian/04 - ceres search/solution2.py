import fileinput


class Board:
    def __init__(self, data: list[str]) -> None:
        self._data = data
        self._w = len(data[0])
        self._h = len(data)

    def scan(self) -> int:
        count = 0
        for y in range(self._h - 2):
            for x in range(self._w - 2):
                if self._match_pattern(x, y):
                    count += 1
        return count

    def _match_pattern(self, x: int, y: int) -> bool:
        a, b = self._data[y][x], self._data[y][x + 2]
        c = self._data[y + 1][x + 1]
        d, e = self._data[y + 2][x], self._data[y + 2][x + 2]

        return (
            c == "A"
            and ((a == "M" and e == "S") or (a == "S" and e == "M"))
            and ((d == "M" and b == "S") or (d == "S" and b == "M"))
        )


def solve(input_file: fileinput.FileInput[str]) -> int:
    board = Board([line.strip() for line in input_file])
    return board.scan()


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

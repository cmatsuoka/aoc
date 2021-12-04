from typing import List, Set, Sequence


class Bingo(Exception):
    def __init__(self):
        super().__init__("Bingo!")


class Board:
    def __init__(self, width: int, height: int, numbers: Sequence[int]):
        self._lines = _extract_lines(width, height, numbers)
        self._columns = _extract_columns(width, height, numbers)

    def mark_number(self, number: int) -> None:
        for line in self._lines:
            line.discard(number)
            if not line:
                raise Bingo()
        for column in self._columns:
            column.discard(number)
            if not column:
                raise Bingo()

    def sum_remaining(self) -> int:
        total = 0
        for line in self._lines:
            print("line =", line)
            total += sum(line)
        return total


def _extract_lines(width: int, height: int, numbers: Sequence[int]) -> List[Set[int]]:
    lines: List[Set[int]] = []
    for i in range(height):
        start = i * width
        ldata = set(numbers[start : start + width])
        lines.append(ldata)
    return lines


def _extract_columns(width: int, height: int, numbers: Sequence[int]) -> List[Set[int]]:
    columns: List[Set[int]] = []
    for j in range(width):
        cdata = set()
        for i in range(height):
            cdata.add(numbers[i * width + j])
        columns.append(cdata)
    return columns

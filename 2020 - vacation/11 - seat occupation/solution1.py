import fileinput
from seats import Seats


class SeatsAdjacent(Seats):
    def _apply_rules(self, i, j):
        seat = self._grid[i][j]
        occupied = self._adjacent_occupied(i, j)

        # rule 1
        if seat == "L" and occupied == 0:
            self._next[i][j] = "#"

        # rule 2
        elif seat == "#" and occupied >= 4:
            self._next[i][j] = "L"

    def _adjacent_occupied(self, row, column):
        people = 0
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x == 0 and y == 0:
                    continue
                i = row + y
                j = column + x
                if i >= 0 and i < self._height and j >= 0 and j < self._width:
                    if self._grid[i][j] == "#":
                        people += 1
        return people


def solve(input_file):
    seats = SeatsAdjacent.from_file(input_file)

    while True:
        seats.move_people()
        if seats.stabilized():
            return seats.count_people()


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

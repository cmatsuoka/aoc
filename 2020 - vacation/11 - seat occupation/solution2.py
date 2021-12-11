import fileinput
from seats import Seats


class SeatsVisible(Seats):
    def _apply_rules(self, i, j):
        seat = self._grid[i][j]

        # rule 1
        if seat == "L" and self._visible_occupied(i, j) == 0:
            self._next[i][j] = "#"

        # rule 2
        elif seat == "#" and self._visible_occupied(i, j) >= 5:
            self._next[i][j] = "L"

    def _visible_occupied(self, row, column):
        people = 0
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x == 0 and y == 0:
                    continue

                # start position
                i = row
                j = column

                while True:
                    i += y
                    j += x
                    if i < 0 or i >= self._height or j < 0 or j >= self._width:
                        break

                    seen = self._grid[i][j]
                    if seen == "#":
                        people += 1
                        break
                    if seen == "L":
                        break

        return people


def solve(input_file):
    seats = SeatsVisible.from_file(input_file)

    while True:
        seats.move_people()
        if seats.stabilized():
            return seats.count_people()


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

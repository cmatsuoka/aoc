import fileinput


_HEADINGS = "NESWNES"


class Ship:
    def __init__(self):
        self._heading = "E"
        self._x = 0
        self._y = 0

    def move(self, cmd, arg):
        if cmd == "N":
            self._y += arg
        elif cmd == "S":
            self._y -= arg
        elif cmd == "E":
            self._x += arg
        elif cmd == "W":
            self._x -= arg
        elif cmd == "F":
            self.move(self._heading, arg)
        elif cmd == "R":
            if arg not in [90, 180, 270]:
                raise RuntimeError("not a right angle turn")

            h = _HEADINGS.index(self._heading)
            self._heading = _HEADINGS[h + int(arg / 90)]
        elif cmd == "L":
            self.move("R", 360 - arg)

    def manhattan(self):
        return abs(self._x) + abs(self._y)


def solve(input_file):
    ship = Ship()

    for line in input_file:
        cmd = line[0]
        arg = int(line[1:])

        ship.move(cmd, arg)

    return ship.manhattan()


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

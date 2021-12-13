import fileinput


class Ship:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._waypoint_x = 10
        self._waypoint_y = 1

    def move(self, cmd, arg):
        if cmd == "N":
            self._waypoint_y += arg
        elif cmd == "S":
            self._waypoint_y -= arg
        elif cmd == "E":
            self._waypoint_x += arg
        elif cmd == "W":
            self._waypoint_x -= arg
        elif cmd == "F":
            self._x += arg * self._waypoint_x
            self._y += arg * self._waypoint_y
        elif cmd == "L":
            if arg not in [90, 180, 270]:
                raise RuntimeError("not a right angle turn")

            x = self._waypoint_x
            y = self._waypoint_y

            self._waypoint_x = x * _cos(arg) - y * _sin(arg)
            self._waypoint_y = x * _sin(arg) + y * _cos(arg)
        elif cmd == "R":
            self.move("L", 360 - arg)

    def manhattan(self):
        return abs(self._x) + abs(self._y)


def _sin(angle):
    return [0, 1, 0, -1, 0][int(angle / 90)]


def _cos(angle):
    return _sin(angle + 90)


def solve(input_file):
    ship = Ship()

    for line in input_file:
        cmd = line[0]
        arg = int(line[1:])

        ship.move(cmd, arg)

    return ship.manhattan()


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

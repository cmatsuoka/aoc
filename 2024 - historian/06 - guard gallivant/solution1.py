import copy
import fileinput


BLOCK = 16
TRACKS = [1, 2, 4, 8]


class Outside(Exception):
    pass


class Blocked(Exception):
    pass


class BeenThere(Exception):
    pass


class Room:
    def __init__(self, m: list[list[str]]) -> None:
        self._h = len(m)
        self._w = len(m[0])

        bm = [[0 for x in range(self._w)] for y in range(self._h)]
        for y in range(self._h):
            for x in range(self._w):
                if m[y][x] == "#":
                    bm[y][x] = BLOCK
                elif m[y][x] == "^":
                    bm[y][x] = 1

        self._m = bm

    def with_block(self, x: int, y: int) -> "Room":
        r = copy.deepcopy(self)
        r._m[y][x] = BLOCK
        return r

    def been_there(self, x: int, y: int, dir: int) -> bool:
        return (self._m[y][x] & TRACKS[dir]) != 0

    def probe(self, x: int, y: int, dir: int) -> tuple[int, int]:
        if dir == 0:  # up
            y -= 1
        elif dir == 1:  # right
            x += 1
        elif dir == 2:  # down
            y += 1
        elif dir == 3:  # left
            x -= 1
        else:
            raise ValueError

        if x < 0 or x >= self._w or y < 0 or y >= self._h:
            raise Outside

        if self._m[y][x] == BLOCK:
            raise Blocked

        return x, y

    def start_point(self) -> tuple[int, int, int]:
        for y in range(self._h):
            for x in range(self._w):
                if self._m[y][x] == 1:
                    return x, y, 0
        raise ValueError

    def mark(self, x: int, y: int, dir: int) -> None:
        self._m[y][x] = self._m[y][x] | TRACKS[dir]


class Guard:
    def __init__(self, x: int, y: int, dir: int) -> None:
        self._x = x
        self._y = y
        self._dir = dir

    def clone(self) -> "Guard":
        return Guard(self._x, self._y, self._dir)

    def location(self) -> tuple[int, int, int]:
        return self._x, self._y, self._dir

    def next_step(self, room: Room) -> tuple[int, int, int]:
        try:
            newx, newy = room.probe(self._x, self._y, self._dir)
            self._x = newx
            self._y = newy
        except Blocked:
            self._dir = (self._dir + 1) % 4

        if room.been_there(self._x, self._y, self._dir):
            raise BeenThere

        return self.location()


def patrol(room: Room, guard: Guard) -> set[tuple[int, int]]:
    path: set[tuple[int, int]] = set()
    loc = guard.location()

    while True:
        try:
            newloc = guard.next_step(room)
            room.mark(*loc)
            path.add((loc[0], loc[1]))
        except Outside:
            path.add((loc[0], loc[1]))
            break

        loc = newloc

    return path


def solve(input_file: fileinput.FileInput[str]) -> int:
    m = [[x for x in line.strip()] for line in input_file]
    room = Room(m)
    guard = Guard(*room.start_point())

    try:
        path = patrol(room, guard)
    except BeenThere:
        path = set()
        pass

    return len(path)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

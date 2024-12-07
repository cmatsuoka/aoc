import copy
import fileinput


BLOCK = 16
TRACKS = [1, 2, 4, 8]


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
        return self._m[y][x] & TRACKS[dir] != 0

    def outside(self, x: int, y: int) -> bool:
        return x < 0 or x >= self._w or y < 0 or y >= self._h

    def blocked(self, x: int, y: int) -> bool:
        if self.outside(x, y):
            return False
        return self._m[y][x] == BLOCK

    def probe(self, x: int, y: int, dir: int) -> tuple[int, int, bool, bool]:
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

        return x, y, self.blocked(x, y), self.outside(x, y)

    def start_point(self) -> tuple[int, int, int]:
        for y in range(self._h):
            for x in range(self._w):
                if self._m[y][x] == 1:
                    return x, y, 0
        raise ValueError

    def mark(self, x: int, y: int, dir: int) -> None:
        self._m[y][x] = self._m[y][x] | TRACKS[dir]

    def visited(self) -> int:
        visited = 0
        for y in range(self._h):
            for x in range(self._w):
                if self._m[y][x] & 0x0F:
                    visited += 1
        return visited

    def dump(self) -> None:
        for y in range(self._h):
            print(" ".join([f"{x:02x}" for x in self._m[y]]))
        print()


class Guard:
    def __init__(self, x: int, y: int, dir: int) -> None:
        self._x = x
        self._y = y
        self._dir = dir

    def clone(self) -> "Guard":
        return Guard(self._x, self._y, self._dir)

    def turn(self) -> None:
        self._dir = (self._dir + 1) % 4

    def walk_to(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def location(self) -> tuple[int, int, int]:
        return self._x, self._y, self._dir


def solve(input_file: fileinput.FileInput[str]) -> int:
    m = [[x for x in line.strip()] for line in input_file]
    room = Room(m)
    guard = Guard(*room.start_point())

    while True:
        loc = guard.location()
        room.mark(*loc)

        newx, newy, blocked, outside = room.probe(*loc)
        if outside:
            break

        if blocked:
            guard.turn()
        else:
            guard.walk_to(newx, newy)

    return room.visited()


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

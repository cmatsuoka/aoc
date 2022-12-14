from dataclasses import dataclass
from typing import List


@dataclass(slots=True)
class Point:
    x: int
    y: int

    @classmethod
    def unmarshal(cls, data: str) -> "Point":
        a, b = data.split(",")
        return cls(int(a), int(b))


def show_field(field: List[List[str]], width: int, height: int) -> None:
    for row in field:
        height -= 1
        if height < 0:
            break
        w2 = width // 2
        print("".join(row[500 - w2 : 500 + w2]))


def draw_line(src: Point, dest: Point, field: List[List[str]]) -> None:
    if src.y == dest.y:
        stride = 1 if dest.x > src.x else -1
        for x in range(src.x, dest.x + stride, stride):
            field[src.y][x] = "#"
    else:
        stride = 1 if dest.y > src.y else -1
        for y in range(src.y, dest.y + stride, stride):
            field[y][src.x] = "#"


def plot(coords: List[Point], field: List[List[str]]) -> None:
    src = coords.pop(0)
    for i in range(len(coords)):
        dest = coords[i]
        draw_line(src, dest, field)
        src = dest

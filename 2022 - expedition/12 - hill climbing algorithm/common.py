import contextlib
import fileinput
import math
from overrides import overrides
from typing import List, Tuple

from astar import AStar  # type: ignore


# A* algorithm implementation from https://github.com/jrialland/python-astar


Node = Tuple[int, int]


class AreaMap(AStar):
    def __init__(
        self,
        input_file: fileinput.FileInput,
    ) -> None:
        self.terrain = [[ord(x) for x in line] for line in input_file]
        self._height = len(self.terrain)
        self._width = len(self.terrain[0])
        self._visited = [[False] * self._width for _ in range(self._height)]

    def locate_point(self, char: str, replace_with: str) -> Node:
        for y in range(self._height):
            row = self.terrain[y]
            with contextlib.suppress(ValueError):
                x = row.index(ord(char))
                row[x] = ord(replace_with)
                break
        else:
            raise RuntimeError("starting point not found")

        return (x, y)

    @overrides
    def heuristic_cost_estimate(self, current: Node, goal: Node) -> float:
        (x1, y1) = current
        (x2, y2) = goal
        return math.hypot(x2 - x1, y2 - y1)

    @overrides
    def distance_between(self, n1: Node, n2: Node) -> float:
        return 1

    @overrides
    def neighbors(self, node: Node) -> List[Node]:
        x, y = node
        reachable: List[Node] = []
        here = self.terrain[y][x]

        # up
        if y > 0 and self.terrain[y - 1][x] <= here + 1:
            reachable.append((x, y - 1))

        # down
        if y < self._height - 1 and self.terrain[y + 1][x] <= here + 1:
            reachable.append((x, y + 1))

        # left
        if x > 0 and self.terrain[y][x - 1] <= here + 1:
            reachable.append((x - 1, y))

        # right
        if x < self._width - 1 and self.terrain[y][x + 1] <= here + 1:
            reachable.append((x + 1, y))

        return reachable

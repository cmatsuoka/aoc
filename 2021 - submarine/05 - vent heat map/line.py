from collections import namedtuple

from heatmap import Heatmap


Point = namedtuple("Point", ["x", "y"])


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def is_diagonal(self) -> bool:
        return abs(self.end.x - self.start.x) == abs(self.end.y - self.start.y)

    def draw(self, canvas: Heatmap) -> None:
        if self.is_vertical():
            self._draw_vertical(canvas)
        elif self.is_horizontal():
            self._draw_horizontal(canvas)
        elif self.is_diagonal():
            self._draw_diagonal(canvas)

    def _draw_vertical(self, canvas: Heatmap) -> None:
        """Optimized line drawer for vertical lines."""
        step = 1 if self.start.y < self.end.y else -1
        for y in range(self.start.y, self.end.y + step, step):
            canvas.add(self.start.x, y)

    def _draw_horizontal(self, canvas: Heatmap) -> None:
        """Optimized line drawer for horizontal lines."""
        step = 1 if self.start.x < self.end.x else -1
        for x in range(self.start.x, self.end.x + step, step):
            canvas.add(x, self.start.y)

    def _draw_diagonal(self, canvas: Heatmap) -> None:
        step_x = cmp(self.end.x, self.start.x)
        step_y = cmp(self.end.y, self.start.y)

        x = self.start.x
        y = self.start.y
        for i in range(abs(self.end.x - self.start.x) + 1):
            canvas.add(x, y)
            x += step_x
            y += step_y


def cmp(a, b):
    return (a > b) - (a < b)

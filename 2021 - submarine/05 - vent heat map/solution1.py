import fileinput

from heatmap import Heatmap
from line import Line, Point


def solve(input_file):
    lines = []

    # parse input
    for input_line in input_file:
        a, b = input_line.split(" -> ")
        x0, y0 = (int(val) for val in a.split(","))
        x1, y1 = (int(val) for val in b.split(","))
        line = Line(start=Point(x0, y0), end=Point(x1, y1))

        if line.is_vertical() or line.is_horizontal():
            lines.append(line)

    canvas = Heatmap(1000, 1000)

    # draw lines
    for line in lines:
        line.draw(canvas)

    return canvas.count(min_value=2)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

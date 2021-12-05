import fileinput

from heatmap import Heatmap
from line import Line, Point


lines = []

# parse input
for input_line in fileinput.input():
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

print(canvas.count(min_value=2))

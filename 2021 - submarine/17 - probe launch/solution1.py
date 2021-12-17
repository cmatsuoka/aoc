import fileinput
import re


def solve(input_file):
    line = input_file.readline()
    m = re.match(r"target area: x=(\d+)\.\.(\d+), y=(-?\d+)\.\.(-?\d+)", line)
    x1, y1 = int(m.group(1)), int(m.group(4))
    x2, y2 = int(m.group(2)), int(m.group(3))

    # Launch reaches y=0 when falling, next iteration must be inside
    # target's y range. Launch y velocity is the previous value. Then
    # find maximum height using the triangular number formula.
    vy = -y2 - 1
    y_max = int(vy * (vy + 1) / 2)

    return y_max


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

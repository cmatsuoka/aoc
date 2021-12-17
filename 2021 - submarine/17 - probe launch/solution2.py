import fileinput
import math
import re


def solve(input_file):
    line = input_file.readline()
    m = re.match(r"target area: x=(\d+)\.\.(\d+), y=(-?\d+)\.\.(-?\d+)", line)
    x1, y1 = int(m.group(1)), int(m.group(4))
    x2, y2 = int(m.group(2)), int(m.group(3))

    # x velocity limits from the triangular number formula
    # sum(k=1,n,k) = n*(n+1)/2
    #
    # minimum x velocity brings the probe to x1
    # maximum x velocity must be inside the target
    vx = lambda x: (-1 + math.sqrt(1 + 8 * x)) / 2
    vx_min = math.ceil(vx(x1))
    vx_max = x2

    # find valid x velocities with points inside the target
    valid_vx = []
    for vel in range(vx_min, vx_max + 1):
        x = 0
        v = vel
        while x <= x2:
            x += v
            if x >= x1 and x <= x2:
                valid_vx.append(vel)
                break
            v -= 1
            if v == 0:
                break

    # simulate launch within valid ranges
    valid = []
    for vel_x in valid_vx:
        for vel_y in range(y2, -y2 + 1):
            x, y = 0, 0
            vx, vy = vel_x, vel_y
            while y >= y2:
                y -= vy
                x += vx
                if x >= x1 and x <= x2 and y <= y1 and y >= y2:
                    valid.append((vel_x, vel_y))
                    break

                if vx > 0:
                    vx -= 1
                vy += 1

    return len(valid)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

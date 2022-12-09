import fileinput


DX = {"L": -1, "R": 1, "U": 0, "D": 0}
DY = {"L": 0, "R": 0, "U": -1, "D": 1}


def solve(input_file):
    knots = 10
    x, y = [0] * knots, [0] * knots
    visited = set()

    for line in input_file:
        (direction, amount) = line.split(" ")
        for _ in range(int(amount)):
            x[0] += DX[direction]
            y[0] += DY[direction]

            for k in range(knots - 1):
                k1 = k + 1

                # deltas
                dx = x[k] - x[k1]
                dy = y[k] - y[k1]
                adx = abs(dx)
                ady = abs(dy)

                if adx > 1 or ady > 1:
                    if adx == ady:     # diagonal
                        x[k1] += dx // adx
                        y[k1] += dy // ady
                    elif adx > ady:    # horizontal
                        x[k1] += dx // adx
                        y[k1] = y[k]
                    else:              # vertical
                        x[k1] = x[k]
                        y[k1] += dy // ady

            visited.add((x[knots - 1], y[knots - 1]))

    return len(visited)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

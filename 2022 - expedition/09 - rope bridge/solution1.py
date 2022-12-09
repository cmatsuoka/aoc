import fileinput


DX = {"L": -1, "R": 1, "U": 0, "D": 0}
DY = {"L": 0, "R": 0, "U": -1, "D": 1}


def solve(input_file):
    hx = hy = tx = ty = 0
    visited = set()

    for line in input_file:
        (direction, amount) = line.split(" ")
        for _ in range(int(amount)):
            hx += DX[direction]
            hy += DY[direction]
        
            if abs(hx - tx) > 1 or abs(hy - ty) > 1:
                if direction in ("L", "R"):
                    tx += DX[direction]
                    ty = hy
                else:
                    tx = hx
                    ty += DY[direction]

            visited.add((tx, ty))

    return len(visited)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

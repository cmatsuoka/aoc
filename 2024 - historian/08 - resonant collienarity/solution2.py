import fileinput
import itertools


def solve(input_file: fileinput.FileInput[str]) -> int:
    pos: dict[str, set[tuple[int, int]]] = {}
    x, y = 0, 0
    for line in input_file:
        x = 0
        for a in line.strip():
            if a != ".":
                if a not in pos:
                    pos[a] = set()
                pos[a].add((x, y))
            x += 1
        y += 1

    w, h = x, y

    nodes: set[tuple[int, int]] = set()
    for _, val in pos.items():
        for a, b in itertools.combinations(val, 2):
            dx = a[0] - b[0]
            dy = a[1] - b[1]

            harm = 0
            while True:
                n1x = a[0] + dx * harm
                n1y = a[1] + dy * harm

                if n1x < 0 or n1x >= w or n1y < 0 or n1y >= h:
                    break

                nodes.add((n1x, n1y))
                harm += 1

            harm = 0
            while True:
                n2x = b[0] - dx * harm
                n2y = b[1] - dy * harm

                if n2x < 0 or n2x >= w or n2y < 0 or n2y >= h:
                    break

                nodes.add((n2x, n2y))
                harm += 1

    return len(nodes)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

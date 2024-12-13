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

            n1x = a[0] + dx
            n1y = a[1] + dy

            if n1x >= 0 and n1x < w and n1y >= 0 and n1y < h:
                nodes.add((n1x, n1y))

            n2x = b[0] - dx
            n2y = b[1] - dy

            if n2x >= 0 and n2x < w and n2y >= 0 and n2y < h:
                nodes.add((n2x, n2y))

    return len(nodes)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

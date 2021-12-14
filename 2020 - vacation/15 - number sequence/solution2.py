import fileinput
import sys


def solve(starting, num):
    pos = {x: i + 1 for i, x in enumerate(starting[:-1])}
    last = starting[-1]
    curr = 0

    for i in range(len(starting), num):
        curr = i - pos[last] if last in pos else 0
        pos[last] = i
        last = curr

    return curr


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} <starting>")
        sys.exit(0)

    starting = [int(x) for x in sys.argv[1].split(",")]
    print(solve(starting, 30000000))

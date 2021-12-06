import fileinput


def solve(input_file):
    pos = 0
    depth = 0

    for line in input_file:
        cmd, arg = line.strip().split(" ", 1)
        val = int(arg)
        if cmd == "forward":
            pos += val
        elif cmd == "down":
            depth += val
        elif cmd == "up":
            depth -= val
            if depth < 0:
                raise RuntimeError("depth is negative")

    return pos * depth


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

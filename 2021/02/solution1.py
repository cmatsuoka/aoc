import fileinput

pos = 0
depth = 0

for line in fileinput.input():
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

print(pos * depth)

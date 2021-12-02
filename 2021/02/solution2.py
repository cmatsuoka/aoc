import fileinput

pos = 0
depth = 0
aim = 0

for line in fileinput.input():
    cmd, arg = line.strip().split(" ", 1)
    val = int(arg)
    if cmd == "forward":
        pos += val
        depth += val * aim
        if depth < 0:
            raise RuntimeError("depth is negative")
    elif cmd == "down":
        aim += val
    elif cmd == "up":
        aim -= val

print(pos * depth)

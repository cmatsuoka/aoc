import fileinput
import re


def solve(input_file):
    mem = {}
    mask = "X" * 36
    addr = val = 0
    for line in input_file:
        if line.startswith("mask = "):
            mask = line.strip()[7:]
        else:
            m = re.match(r"mem\[([0-9]+)\] = ([0-9]+)", line)
            addr = int(m.group(1))
            val = int(m.group(2))

            for a in _apply_mask(mask, addr):
                mem[a] = val
    return sum(mem.values())


def _apply_mask(mask, addr):
    or_mask = int(mask.replace("X", "0"), 2)
    x_mask = int(mask.replace("1", "0").replace("X", "1"), 2)
    count = mask.count("X")

    addr |= or_mask
    addr &= ~x_mask

    addrs = []
    x_pos = [x for x in range(35, -1, -1) if x_mask & (1 << x)]

    # expand floating bits
    for i in range(2 ** count):
        my_addr = addr
        for j in range(count):
            bit = (i >> (count - j - 1)) & 1
            my_addr |= bit << x_pos[j]
        addrs.append(my_addr)

    return addrs


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

import fileinput
import re


def solve(input_file):
    mem = {}
    mask = "X" * 36
    addr = val = 0
    for line in input_file:
        if line.startswith("mask = "):
            mask = line[7:]
        else:
            m = re.match(r"mem\[([0-9]+)\] = ([0-9]+)", line)
            addr = int(m.group(1))
            val = int(m.group(2))
            mem[addr] = _apply_mask(mask, val)
    return sum(mem.values())


def _apply_mask(mask, val):
    or_mask = int(mask.replace("X", "0"), 2)
    and_mask = int(mask.replace("X", "1"), 2)
    return (val & and_mask) | or_mask


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

import fileinput
import re

INS_RE = re.compile(r"^([a-z][a-z']{1,4})\((?:(\d+),(\d+))?\)")


def solve(input_file: fileinput.FileInput[str]) -> int:
    data = "".join(list(input_file))
    enabled = True

    total = 0
    for i in range(len(data)):
        parm = INS_RE.findall(data[i:])
        if not parm:
            continue
        (ins, arg1, arg2) = parm[0]
        if ins == "mul" and arg1 and arg2:
            if enabled:
                total += int(arg1) * int(arg2)
        elif ins == "do":
            enabled = True
        elif ins == "don't":
            enabled = False

    return total


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

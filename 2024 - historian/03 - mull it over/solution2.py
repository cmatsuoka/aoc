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
        if parm[0][0] == "mul":
            if enabled:
                total += int(parm[0][1]) * int(parm[0][2])
        elif parm[0][0] == "do":
            enabled = True
        elif parm[0][0] == "don't":
            enabled = False

    return total


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

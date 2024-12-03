import fileinput
import re

INS_RE = re.compile(r"^mul\((\d+),(\d+)\)")


def solve(input_file: fileinput.FileInput[str]) -> int:
    data = "".join(list(input_file))

    total = 0
    for i in range(len(data)):
        parm = INS_RE.findall(data[i:])
        if parm:
            total += int(parm[0][0]) * int(parm[0][1])

    return total


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

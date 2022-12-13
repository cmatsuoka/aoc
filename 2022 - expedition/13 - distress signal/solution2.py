import fileinput
import functools
from typing import Any, Dict, List


def _is_lower(left: List, right: List) -> int:
    if isinstance(left, int) and isinstance(right, int):
        if left != right:
            return -1 if left < right else 1
        return 0

    if isinstance(left, int):
        left = [left]

    if isinstance(right, int):
        right = [right]

    for e1, e2 in zip(left, right):
        if e1 != e2:
            check = _is_lower(e1, e2)
            if check != 0:
                return check

    if len(left) != len(right):
        return -1 if len(left) < len(right) else 1

    return 0


def solve(input_file: fileinput.FileInput) -> int:
    sep = "\n"
    packets = [[[2]], [[6]]]

    while sep:
        left = input_file.readline().strip()
        right = input_file.readline().strip()
        sep = input_file.readline()

        # It's not my fault that input packets are also valid Python lists
        res: Dict[str, Any] = {}
        exec(f"left={left}", globals(), res)
        exec(f"right={right}", globals(), res)

        packets.append(res["left"])
        packets.append(res["right"])

    packets.sort(key=functools.cmp_to_key(_is_lower))

    pos1 = packets.index([[2]]) + 1
    pos2 = packets.index([[6]]) + 1

    return pos1 * pos2


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

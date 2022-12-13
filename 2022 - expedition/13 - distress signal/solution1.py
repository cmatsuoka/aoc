import fileinput
from typing import Any, Dict, List, Optional


def _is_lower(left: List, right: List) -> Optional[bool]:
    if isinstance(left, int) and isinstance(right, int):
        if left != right:
            return left < right
        return None

    if isinstance(left, int):
        left = [left]

    if isinstance(right, int):
        right = [right]

    for e1, e2 in zip(left, right):
        if e1 != e2:
            check = _is_lower(e1, e2)
            if check is not None:
                return check

    if len(left) != len(right):
        return len(left) < len(right)

    return None


def solve(input_file: fileinput.FileInput) -> int:
    total = 0
    index = 1
    sep = "\n"

    while sep:
        left = input_file.readline().strip()
        right = input_file.readline().strip()
        sep = input_file.readline()

        # It's not my fault that input packets are also valid Python lists
        res: Dict[str, Any] = {}
        exec(f"left={left}", globals(), res)
        exec(f"right={right}", globals(), res)

        if _is_lower(res["left"], res["right"]):
            total += index

        index += 1

    return total


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

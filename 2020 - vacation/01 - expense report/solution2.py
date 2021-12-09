import fileinput
from typing import Optional, Set, Tuple


def _find_addends(sum_value: int, entries: Set[int]) -> Optional[Tuple[int, int]]:
    while True:
        try:
            x = entries.pop()
        except KeyError:
            break

        complement = sum_value - x
        if complement in entries:
            return (x, complement)

    return None


def solve(input_file):
    entries = [int(x) for x in input_file]

    for i in range(len(entries)):
        candidate = entries[i]
        sum_value = 2020 - candidate

        addends = _find_addends(sum_value, set(entries[i + 1 :]))
        if addends:
            return candidate * addends[0] * addends[1]
            break

    return None


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

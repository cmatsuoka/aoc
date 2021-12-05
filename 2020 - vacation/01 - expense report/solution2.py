import fileinput
from typing import Optional, Set, Tuple


entries = []
for line in fileinput.input():
    entries.append(int(line))


def find_addends(sum_value: int, entries: Set[int]) -> Optional[Tuple[int, int]]:
    while True:
        try:
            x = entries.pop()
        except KeyError:
            break

        complement = sum_value - x
        if complement in entries:
            return (x, complement)

    return None


for i in range(len(entries)):
    candidate = entries[i]
    sum_value = 2020 - candidate

    addends = find_addends(sum_value, set(entries[i + 1:]))
    if addends:
        print(f"{candidate} + {addends[0]} + {addends[1]} = {candidate + addends[0] + addends[1]}")
        print(f"{candidate} * {addends[0]} * {addends[1]} = {candidate * addends[0] * addends[1]}")
        break

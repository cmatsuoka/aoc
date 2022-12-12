import fileinput
from typing import List

import common


def solve(input_file: fileinput.FileInput) -> int:
    possible_paths: List[int] = []

    my_map = common.AreaMap(input_file)
    end = my_map.locate_point("E", replace_with="z")

    for y, row in enumerate(my_map.terrain):
        for x, column in enumerate(row):
            if column == ord("a"):
                start = (x, y)

                path = my_map.astar(start, end)
                if path:
                    possible_paths.append(len(list(path)) - 1)

    return sorted(possible_paths)[0]


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

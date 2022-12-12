import fileinput

import common


def solve(input_file: fileinput.FileInput) -> int:
    my_map = common.AreaMap(input_file)

    # locate starting point
    start = my_map.locate_point("S", replace_with="a")
    end = my_map.locate_point("E", replace_with="z")
    path = list(my_map.astar(start, end))
    return len(path) - 1


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

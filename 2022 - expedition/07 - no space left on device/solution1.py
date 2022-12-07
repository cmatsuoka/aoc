import fileinput

import common


def solve(input_file):
    filesystem = common.Filesystem()
    filesystem.parse(input_file)
    filesystem.add_sizes(threshold=100000)
    return filesystem.sum_below_threshold


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

import fileinput

import common


def solve(input_file):
    filesystem = common.Filesystem()
    filesystem.parse(input_file)
    filesystem.add_sizes()

    used_space = filesystem.get_used_space()
    delete_target = 30000000 - (70000000 - used_space)

    return filesystem.dir_to_delete(space_to_free=delete_target)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

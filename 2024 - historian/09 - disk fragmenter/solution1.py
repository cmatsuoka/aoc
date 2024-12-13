import fileinput


def dump(disk: list[int]):
    s = ""
    for block in disk:
        s += "." if block < 0 else str(block)
    print(s)


def solve(input_file: fileinput.FileInput[str]) -> int:
    disk: list[int] = []

    id = 0
    isfile = True

    for length in input_file.readline().strip():
        if isfile:
            disk.extend([id] * int(length))
            id += 1
        else:
            disk.extend([-1] * int(length))
        isfile = isfile ^ True

    size = len(disk)
    get_cursor = size - 1
    put_cursor = 0

    while disk[put_cursor] >= 0:
        put_cursor += 1

    while put_cursor < get_cursor:
        block = disk[get_cursor]
        disk[get_cursor] = -1
        if block < 0:
            get_cursor -= 1
            continue

        disk[put_cursor] = block
        while disk[put_cursor] >= 0:
            put_cursor += 1

    checksum = 0
    for i, block in enumerate(disk):
        if block < 0:
            break
        checksum += i * block

    return checksum


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

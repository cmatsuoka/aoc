import fileinput
from dataclasses import dataclass


@dataclass
class Chunk:
    id: int
    length: int


def dump(disk: list[Chunk]) -> None:
    s = ""
    for chunk in disk:
        char = "." if chunk.id < 0 else str(chunk.id)
        s += char * chunk.length
    print(s)


def solve(input_file: fileinput.FileInput[str]) -> int:
    disk: list[Chunk] = []
    fileid = 0
    isfile = True
    for length in input_file.readline().strip():
        if isfile:
            disk.append(Chunk(int(fileid), int(length)))
            fileid += 1
        else:
            disk.append(Chunk(-1, int(length)))
        isfile = isfile ^ True

    dump(disk)

    first_empty = 1  # first chunk with empty blocks

    get_index = len(disk) - 1
    put_index = 1

    while get_index > put_index:
        put_chunk = disk[put_index]
        put_size = put_chunk.length

        get_chunk = disk[get_index]
        get_size = get_chunk.length

        if get_size > put_size:
            get_index -= 2
            continue

        put_chunk.id = get_chunk.id
        put_chunk.length = get_chunk.length

        get_chunk.id = -1

        hole_size = put_size - get_size

        if hole_size > 0:
            new_chunk = Chunk(-1, hole_size)
            disk = disk[: put_index + 1] + [new_chunk] + disk[put_index + 1 :]
            put_index += 1
            get_index += 1

        put_index += 2
        get_index -= 2

        dump(disk)

    dump(disk)

    return 0


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

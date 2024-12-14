import fileinput
from dataclasses import dataclass


@dataclass
class Chunk:
    id: int
    length: int


def checksum(disk: list[Chunk]) -> int:
    sum = 0
    block = 0
    for chunk in disk:
        for b in range(chunk.length):
            if chunk.id > 0:
                sum += block * chunk.id
            block += 1
    return sum


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

    get_index = len(disk) - 1
    while get_index >= 2:
        get_chunk = disk[get_index]
        if get_chunk.id < 0:
            get_index -= 1
            continue

        get_size = get_chunk.length

        for put_index in range(1, get_index):
            put_chunk = disk[put_index]
            put_size = put_chunk.length

            if put_chunk.id != -1:
                put_index += 1
                continue

            if get_size > put_size:
                put_index += 1
                continue

            put_chunk.id = get_chunk.id
            put_chunk.length = get_chunk.length

            get_chunk.id = -1

            hole_size = put_size - get_size

            if hole_size > 0:
                new_chunk = Chunk(-1, hole_size)
                disk = disk[: put_index + 1] + [new_chunk] + disk[put_index + 1 :]
                put_index += 1

            put_index += 1

            break

        get_index -= 1

    return checksum(disk)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

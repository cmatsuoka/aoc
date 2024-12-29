import fileinput

from solution1 import Room, Guard, Outside, BeenThere, patrol


def solve(input_file: fileinput.FileInput[str]) -> int:
    m = [[x for x in line.strip()] for line in input_file]
    room = Room(m)
    guard = Guard(*room.start_point())

    try:
        path = patrol(room, guard)
    except BeenThere:
        path = set()
        pass

    obstacles = 0

    for x, y in path:
        room = Room(m)
        guard = Guard(*room.start_point())
        room = room.with_block(x, y)

        try:
            patrol(room, guard)
        except Outside:
            pass
        except BeenThere:
            obstacles += 1

    return obstacles


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

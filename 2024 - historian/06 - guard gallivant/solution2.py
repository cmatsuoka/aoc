import fileinput

from solution1 import Guard, Room


def patrol(room: Room, guard: Guard, *, in_multiverse: bool = False) -> int:
    obstacles = 0
    while True:
        loc = guard.location()
        room.mark(*loc)

        newx, newy, blocked, outside = room.probe(*loc)
        if outside:
            break

        if blocked:
            guard.turn()
        else:
            if in_multiverse:
                if room.been_there(newx, newy, loc[2]):
                    return 1
            else:
                room2 = room.with_block(newx, newy)
                guard2 = guard.clone()
                obstacles += patrol(room2, guard2, in_multiverse=True)
            guard.walk_to(newx, newy)

    return obstacles


def solve(input_file: fileinput.FileInput[str]) -> int:
    m = [[x for x in line.strip()] for line in input_file]
    room = Room(m)
    guard = Guard(*room.start_point())

    return patrol(room, guard)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

import fileinput

from solution1 import Guard, Room


def patrol_multiverse(room: Room, guard: Guard) -> bool:
    guard.turn()
    while True:
        loc = guard.location()
        print("MULTIVERSE location:", *loc)
        if room.been_there(*loc):
            print("BEEN THERE!")
            return True

        room.mark(*loc)

        newx, newy, blocked, outside = room.probe(*loc)
        if outside:
            break

        if blocked:
            guard.turn()
        else:
            guard.walk_to(newx, newy)

    return False


def solve(input_file: fileinput.FileInput[str]) -> int:
    m = [[x for x in line.strip()] for line in input_file]
    room = Room(m)
    guard = Guard(*room.start_point())

    obstacles = 0
    while True:
        loc = guard.location()
        room.mark(*loc)
        print("location:", *loc)

        newx, newy, blocked, outside = room.probe(*loc)
        if outside:
            break

        if blocked:
            guard.turn()
        else:
            if patrol_multiverse(room.with_block(newx, newy), guard.clone()):
                print("LOOPED")
                obstacles += 1
            guard.walk_to(newx, newy)

    return obstacles


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

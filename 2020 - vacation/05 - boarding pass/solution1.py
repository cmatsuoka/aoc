import fileinput


def _decode(code: str) -> int:
    seat = 0
    for i in range(10):
        if code[i] == "B":
            seat |= 0x200 >> i
        elif code[i] == "R":
            seat |= 0x04 >> (i - 7)
    return seat


def solve(input_file):
    max_id = 0
    for line in input_file:
        seat_id = _decode(line)
        if seat_id > max_id:
            max_id = seat_id

    return max_id


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

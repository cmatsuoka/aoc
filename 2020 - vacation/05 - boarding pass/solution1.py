import fileinput


def decode(code: str) -> int:
    seat = 0
    for i in range(10):
        if code[i] == "B":
            seat |= (0x200 >> i)
        elif code[i] == "R":
            seat |= (0x04 >> (i - 7))
    return seat

max_id = 0
for line in fileinput.input():
    seat_id = decode(line)
    if seat_id > max_id:
        max_id = seat_id

print(max_id)


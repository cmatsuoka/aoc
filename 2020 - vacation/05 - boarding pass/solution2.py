import fileinput


empty_seats = set(range(0x400))

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
    empty_seats.remove(seat_id)

for seat in empty_seats:
    if (seat - 1) not in empty_seats and (seat + 1) not in empty_seats:
        print(seat)
        break

import fileinput

import bingo

WIDTH = 5
HEIGHT = 5

data = fileinput.input()

# read and parse number sequence
numseq = next(data)
draw_sequence = [int(n) for n in numseq.split(",")]

# read and parse boards
bnum = 0
boards = []
winning_boards = set()

for sep in data:
    if sep.strip():
        raise RuntimeError("missing separator line")

    numbers = []
    for i in range(HEIGHT):
        line = next(data)
        line_numbers = [int(n) for n in line.split()]
        if len(line_numbers) != WIDTH:
            raise RuntimeError(f"board {bnum} line {i} has wrong number of columns")
        numbers.extend(line_numbers)

    board = bingo.Board(WIDTH, HEIGHT, numbers)
    boards.append(board)
    bnum += 1

print(f"{bnum} boards loaded")

# execute bingo
for num in draw_sequence:
    print(f"draw number {num}")
    for b, board in enumerate(boards):
        if board in winning_boards:
            continue

        try:
            board.mark_number(num)
        except bingo.Bingo as err:
            print(f"{err} in board {b}")
            last_board = board
            last_num = num
            winning_boards.add(board)

    if len(winning_boards) == bnum:
         print("this is the last board")
         break
            
remaining = last_board.sum_remaining()
print("remaining sum =", remaining)
print("last draw =", last_num)
print("score =", remaining * last_num)

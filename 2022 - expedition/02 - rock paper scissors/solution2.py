import fileinput

# 3x3 matrix containing player score according to instruction
PLAYER_SCORE = ((3, 1, 2), (1, 2, 3), (2, 3, 1))

# match score according to instruction
WIN_SCORE = (0, 3, 6)


def solve(input_file):
    score = 0

    for line in input_file:
        opponent = ord(line[0]) - ord("A")
        instruction = ord(line[2]) - ord("X")
        score += PLAYER_SCORE[opponent][instruction] + WIN_SCORE[instruction]

    return score


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

import fileinput


# player score according to player's choice
PLAYER_SCORE = (1, 2, 3)

# 3x3 matrix containing match score according to player's choice
WIN_SCORE = ((3, 6, 0), (0, 3, 6), (6, 0, 3))


def solve(input_file):
    score = 0

    for line in input_file:
        opponent = ord(line[0]) - ord("A")
        player = ord(line[2]) - ord("X")
        score += PLAYER_SCORE[player] + WIN_SCORE[opponent][player]

    return score


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

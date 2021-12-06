import fileinput
import string


def solve(input_file):
    all_answers = set(string.ascii_lowercase)

    total = 0
    answers = all_answers

    for line in input_file:
        line = line.strip()
        if line:
            this_answer = set(line)
            answers = answers.intersection(this_answer)
            continue

        total += len(answers)
        answers = all_answers

    total += len(answers)

    return total


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

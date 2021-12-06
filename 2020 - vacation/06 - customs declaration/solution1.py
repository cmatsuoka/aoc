import fileinput


def solve(input_file):
    total = 0
    answers = set()

    for line in input_file:
        line = line.strip()
        if line:
            for question in line:
                answers.add(question)
            continue

        total += len(answers)
        answers.clear()

    total += len(answers)

    return total


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

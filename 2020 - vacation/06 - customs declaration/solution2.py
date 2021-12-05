import fileinput
import string


all_answers = set(string.ascii_lowercase)

total = 0
answers = all_answers

for line in fileinput.input():
    line = line.strip()
    if line:
        this_answer = set(line)
        answers = answers.intersection(this_answer)
        continue

    total += len(answers)
    answers = all_answers

total += len(answers)

print(total)

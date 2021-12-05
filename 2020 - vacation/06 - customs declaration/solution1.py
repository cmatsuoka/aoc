import fileinput


total = 0
answers = set()

for line in fileinput.input():
    line = line.strip()
    if line:
        for question in line:
            answers.add(question)
        continue

    total += len(answers)
    answers.clear()

total += len(answers)

print(total)

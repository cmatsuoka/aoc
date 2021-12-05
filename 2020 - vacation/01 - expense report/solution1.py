import fileinput

entries = set()
for line in fileinput.input():
    entries.add(int(line))

while True:
    try:
        x = entries.pop()
    except KeyError:
        break

    complement = 2020 - x
    if complement in entries:
        print(f"{x} + {complement} = {x + complement}")
        print(f"{x} * {complement} = {x * complement}")
        break

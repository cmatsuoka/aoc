import fileinput

data = fileinput.input()

prev = next(data)

incs = 0

for curr in data:
    if int(curr) > int(prev):
        incs += 1
    prev = curr

print(incs)

import fileinput

data = fileinput.input()

line = next(data)
d0 = int(line)

line = next(data)
d1 = int(line)

line = next(data)
d2 = int(line)

prev = d0 + d1 + d2

d0 = d1
d1 = d2

incs = 0

for line in data:
    d2 = int(line)
    curr = d0 + d1 + d2
    if curr > prev:
        incs += 1
    d0 = d1
    d1 = d2
    prev = curr

print(incs)

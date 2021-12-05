import fileinput


valid = 0
for line in fileinput.input():
    policy, password = line.split(": ")
    count, char = policy.split()
    pos1, pos2 = (int(x) for x in count.split("-"))

    if (password[pos1 - 1] == char) ^ (password[pos2 - 1] == char):
        valid += 1

print(valid)

import fileinput


valid = 0
for line in fileinput.input():
    policy, password = line.split(": ")
    count, char = policy.split()
    low, high = (int(x) for x in count.split("-"))
    actual = password.count(char)

    if actual >= low and actual <= high:
        valid += 1

print(valid)

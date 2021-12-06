import fileinput


def solve(input_file):
    valid = 0
    for line in input_file:
        policy, password = line.split(": ")
        count, char = policy.split()
        low, high = (int(x) for x in count.split("-"))
        actual = password.count(char)

        if actual >= low and actual <= high:
            valid += 1

    return valid


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

import fileinput


def solve(file_input):
    line = file_input.readline().strip()

    school = [int(x) for x in line.split(",")]

    # a very inefficient way to process this data
    for _ in range(80):
        num = len(school)
        for i in range(num):
            school[i] -= 1
            if school[i] < 0:
                school.append(8)
                school[i] = 6

    return len(school)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

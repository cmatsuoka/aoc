import fileinput


def solve(input_file: fileinput.FileInput[str]) -> int:
    list1: list[int] = []
    list2: list[int] = []

    for line in input_file:
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))

    return sum(map(lambda x: x * list2.count(x), list1))


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

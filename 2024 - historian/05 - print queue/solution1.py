import fileinput


def solve(input_file: fileinput.FileInput[str]) -> int:
    rules: list[tuple[int, ...]] = []
    for line in input_file:
        line = line.strip()
        if line == "":
            break
        rules.append(tuple([int(x) for x in line.split("|")]))

    sum = 0
    for line in input_file:
        line = line.strip()
        pages = [int(x) for x in line.split(",")]
        for i, p in enumerate(pages):
            before = pages[:i]
            after = pages[i + 1 :]
            for p0, p1 in rules:
                if p0 == p:
                    if p1 in before:
                        break
                elif p1 == p:
                    if p0 in after:
                        break
            else:
                continue
            break
        else:
            sum += pages[len(pages) // 2]

    return sum


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

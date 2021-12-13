import fileinput


def solve(input_file):
    timestamp = int(input_file.readline())

    entries = []
    next_times = []
    for entry in input_file.readline().split(","):
        if entry == "x":  # ignore for now
            continue

        num = int(entry)
        entries.append(num)
        next_times.append(num * (int(timestamp / num) + 1))

    my_time = min(next_times)
    index = next_times.index(my_time)

    return entries[index] * (my_time - timestamp)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

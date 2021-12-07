import fileinput
import statistics


def solve(input_file):
    positions = [int(x) for x in input_file.readline().split(",")]
    median = statistics.median(positions)

    if int(median) != median:
        print(f"median value is {median}")

    total = 0
    for pos in positions:
        total += abs(pos - median)

    return int(total)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

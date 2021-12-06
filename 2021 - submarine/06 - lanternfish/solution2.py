import fileinput

def solve(file_input):
    line = file_input.readline().strip()

    school = [int(x) for x in line.split(",")]

    # populate a breeding table
    # each item shows the number of fish breeding in that amount of days
    breeding_table = [0] * 9
    for fish in school:
        breeding_table[fish] += 1

    for day in range(256):
        # the amount of fish breeding today, and advance the table one day
        breeding = breeding_table.pop(0)
        breeding_table.append(0)

        # new fish will breed in 9 days
        breeding_table[8] = breeding

        # existing fish will breed again in 7 days
        breeding_table[6] += breeding

    return sum(breeding_table)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

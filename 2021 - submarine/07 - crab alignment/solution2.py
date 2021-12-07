import fileinput
import statistics


def solve(input_file):
    positions = [int(x) for x in input_file.readline().split(",")]
    positions.sort()

    min_fuel = 999999999999999999

    for candidate in range(max(positions)):
        fuel = _fuel_for_position(candidate, positions)
        if fuel < min_fuel:
            min_fuel = fuel
        else:
            break

    return min_fuel


def _fuel_for_position(pos, positions):
    fuel = 0
    for i in positions:
        dev = abs(pos - i)
        fuel += int((dev / 2) * (1 + dev))

    return fuel


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

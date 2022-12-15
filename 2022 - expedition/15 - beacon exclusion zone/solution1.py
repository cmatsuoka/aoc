import fileinput
import re
from dataclasses import dataclass
from typing import List


@dataclass
class Sensor:
    x: int
    y: int
    radius: int


def solve(input_file: fileinput.FileInput, *, target_y: int) -> int:
    sensors: List[Sensor] = []
    beacons: Set[Tuple[int, int]] = set()

    for line in input_file:
        parts = re.split(r"[ :=,\n]+", line)
        x, y = int(parts[3]), int(parts[5])
        bx, by = int(parts[11]), int(parts[13])
        radius = abs(bx - x) + abs(by - y)
         
        sensors.append(Sensor(x, y, radius))
        beacons.add((bx, by))

    # count the beacons we have on row target_y:
    num_beacons = len([b for b in beacons if b[1] == target_y])

    # filter the sensors that cover row target_y
    sensors = [s for s in sensors if abs(s.y - target_y) <= s.radius]

    # check coverage range of each filtered sensor in row target_y
    extents: List[Tuple[int, int]] = []
    for sensor in sensors:
        distance_x =  sensor.radius - abs(sensor.y - target_y)
        extents.append((sensor.x - distance_x, sensor.x + distance_x))

    # compute total coverage of all extents
    # each range limit is the x coordinate of start or end and if is end
    # then sort limits and iterate counting covered extents
    limits: List[Tuple[int, bool]] = []
    for extent in extents:
        limits.append((extent[0], False))
        limits.append((extent[1], True))

    # iterate on sorted limits and see when a extent is not covered
    level = 0
    count = 0

    prev_start: int
    for limit in sorted(limits):
        if limit[1]:  # end of extent
            level -= 1
            if level == 0:
                count += limit[0] - prev_start + 1
        else:  # start of extent
            level += 1
            if level == 1:
                prev_start = limit[0]

    return count - num_beacons


if __name__ == "__main__":
    print(solve(fileinput.FileInput(), target_y=2000000))

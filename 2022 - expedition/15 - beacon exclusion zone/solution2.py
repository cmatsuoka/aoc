import fileinput
import re
from dataclasses import dataclass
from typing import List


@dataclass(slots=True)
class Sensor:
    x: int
    y: int
    radius: int


@dataclass(slots=True)
class Segment:
    start_x: int
    start_y: int
    dx: int
    dy: int
    size: int

    # This looks a bit ugly
    def crop(self, max_coord: int) -> "Segment":
        if self.start_x < 0:
            delta = -self.start_x
            self.size -= delta
            self.start_y += delta  # dx is always 1
            self.start_x = 0

        if self.start_x + self.size > max_coord:
            delta = self.start_x + self.size - max_coord
            self.size -= delta

        if self.dy > 0:
            if self.start_y < 0:
                delta = -self.start_y
                self.size -= delta
                self.start_x += delta
                self.start_y = 0

            if self.start_y + self.size > max_coord:
                delta = self.start_y + self.size - max_coord
                self.size -= delta
        else:
            if self.start_y > max_coord:
                delta = self.start_y - max_coord
                self.size -= delta
                self.start_y = max_coord
                self.start_x += delta

            if self.start_y - self.size < 0:
                delta = -(self.start_y - self.size)
                self.size -= delta

        return self


# This still takes some time to run and can probably be further
# optimized, but I'll stop here and declare it's good enough.


def solve(input_file: fileinput.FileInput, max_coord: int) -> int:
    sensors: List[Sensor] = []

    for line in input_file:
        parts = re.split(r"[ :=,\n]+", line)
        x, y = int(parts[3]), int(parts[5])
        bx, by = int(parts[11]), int(parts[13])
        radius = abs(bx - x) + abs(by - y)
        sensors.append(Sensor(x, y, radius))

    # Insight: the missing beacon must be in a position neighboring an
    # existing coverage area
    sensor_candidates: List[List[Segment]] = []
    for sensor in sensors:
        new_radius = sensor.radius + 1
        top_x, top_y = sensor.x, sensor.y - new_radius
        bottom_x, bottom_y = sensor.x, sensor.y + new_radius
        left_x, left_y = sensor.x - new_radius, sensor.y

        if left_x > max_coord or left_x + sensor.radius < 0:
            continue

        if top_y > max_coord or top_y + sensor.radius < 0:
            continue

        # store segment definitions for each candidate area, they're too
        # large to store as a list of locations
        sensor_candidates.append(
            [
                Segment(left_x, left_y, 1, -1, sensor.radius).crop(max_coord),
                Segment(top_x, top_y, 1, 1, sensor.radius).crop(max_coord),
                Segment(left_x, left_y, 1, 1, sensor.radius).crop(max_coord),
                Segment(bottom_x, bottom_y, 1, -1, sensor.radius).crop(max_coord),
            ]
        )

    # Now we check which points of those candidate segments are not inside any
    # covered area
    for j, candidates in enumerate(sensor_candidates):
        for _, candidate in enumerate(candidates):
            for k in range(candidate.size):
                x, y = (
                    candidate.start_x + k * candidate.dx,
                    candidate.start_y + k * candidate.dy,
                )

                for i, sensor in enumerate(sensors):
                    if i == j:
                        # neighbors are not covered by the corresponding sensor
                        continue

                    # check neighbor locations to see if its covered by this sensor
                    dx = abs(sensor.x - x)
                    dy = abs(sensor.y - y)
                    if (dx + dy) <= sensor.radius:
                        # it's inside one of the sensor areas
                        break
                else:
                    # not covered by any sensor!
                    print(x, y)
                    return x * 4000000 + y

    raise RuntimeError("beacon not found")


if __name__ == "__main__":
    print(solve(fileinput.FileInput(), max_coord=4000000))

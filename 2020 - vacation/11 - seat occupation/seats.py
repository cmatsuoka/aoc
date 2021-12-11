import abc
import copy


class Seats(abc.ABC):
    def __init__(self, data):
        self._grid = None
        self._next = data
        self._width = len(data[0])
        self._height = len(data)

    def stabilized(self):
        for i in range(self._height):
            if self._grid[i] != self._next[i]:
                return False
        return True

    @classmethod
    def from_file(cls, input_file):
        data = []
        for line in input_file:
            data.append(list(line.strip()))
        return cls(data)

    def move_people(self):
        self._grid = copy.deepcopy(self._next)

        for i in range(self._height):
            for j in range(self._width):
                self._apply_rules(i, j)

    @abc.abstractmethod
    def _apply_rules(self, i, j):
        pass

    def count_people(self):
        people = 0
        for i in range(self._height):
            people += self._grid[i].count("#")
        return people

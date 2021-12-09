class HeightMap:
    def __init__(self, data):
        self._data = data
        self.height = len(data)
        self.width = len(data[0])
        self._last_x = self.width - 1
        self._last_y = self.height - 1

    @classmethod
    def from_file(cls, input_file):
        data = []
        for line in input_file:
            data.append([int(x) for x in line.strip()])
        return cls(data)

    def _lower_than_up(self, x, y):
        if y <= 0:
            return True
        return self._data[y][x] < self._data[y - 1][x]

    def _lower_than_down(self, x, y):
        if y >= self._last_y:
            return True
        return self._data[y][x] < self._data[y + 1][x]

    def _lower_than_left(self, x, y):
        if x <= 0:
            return True
        return self._data[y][x] < self._data[y][x - 1]

    def _lower_than_right(self, x, y):
        if x >= self._last_x:
            return True
        return self._data[y][x] < self._data[y][x + 1]

    def is_lowpoint(self, x, y):
        return (
            self._lower_than_up(x, y)
            and self._lower_than_down(x, y)
            and self._lower_than_left(x, y)
            and self._lower_than_right(x, y)
        )

    def value(self, x, y):
        return self._data[y][x]

    def peek_up(self, x, y):
        if y <= 0:
            return False
        return self._data[y - 1][x] < 9

    def peek_down(self, x, y):
        if y >= self._last_y:
            return False
        return self._data[y + 1][x] < 9

    def peek_left(self, x, y):
        if x <= 0:
            return False
        return self._data[y][x - 1] < 9

    def peek_right(self, x, y):
        if x >= self._last_x:
            return False
        return self._data[y][x + 1] < 9

    def flood(self, x, y):
        size = 1
        self._data[y][x] = 10

        if self.peek_up(x, y):
            size += self.flood(x, y - 1)
        if self.peek_down(x, y):
            size += self.flood(x, y + 1)
        if self.peek_left(x, y):
            size += self.flood(x - 1, y)
        if self.peek_right(x, y):
            size += self.flood(x + 1, y)

        return size

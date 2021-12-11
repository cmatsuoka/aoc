class Grid:
    def __init__(self, data):
        self._grid = data
        self._width = len(data[0])
        self._height = len(data)
        self.flashes = 0
        self.all_flashed = False

        self._flashed = []
        for _ in range(self._height):
            self._flashed.append([False] * self._width)

    @classmethod
    def from_file(cls, input_file):
        data = []
        for line in input_file:
            data.append([int(x) for x in line.strip()])
        return cls(data)

    def do_cycle(self):
        self._do_increment()

        while True:
            flashes = self.flashes
            self._do_flash()
            if flashes == self.flashes:
                break

        self.all_flashed = self._check_simultaneous()

        self._do_reset()

    def _do_increment(self):
        for i in range(self._height):
            for j in range(self._width):
                self._grid[i][j] += 1

    def _do_flash(self):
        for i in range(self._height):
            for j in range(self._width):
                if not self._flashed[i][j] and self._grid[i][j] > 9:
                    self._propagate(i, j)
                    self._flashed[i][j] = True
                    self.flashes += 1

    def _check_simultaneous(self):
        for i in range(self._height):
            for j in range(self._width):
                if not self._flashed[i][j]:
                    return False
        return True

    def _do_reset(self):
        for i in range(self._height):
            for j in range(self._width):
                if self._grid[i][j] > 9:
                    self._grid[i][j] = 0
                    self._flashed[i][j] = False

    def _propagate(self, row, column):
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                i = row + y
                j = column + x
                if i >= 0 and i < self._height and j >= 0 and j < self._width:
                    self._grid[i][j] += 1

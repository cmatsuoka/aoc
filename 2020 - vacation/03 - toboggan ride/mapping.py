class Map:
    def __init__(self, data):
        self._data = data
        self._pos_x = 0
        self._pos_y = 0
        self._width = len(data[0])
        self._height = len(data)

    @classmethod
    def from_file(cls, input_file):
        data = []
        for line in input_file:
            data.append(line.strip())
        return Map(data)

    def walk(self, inc_x, inc_y):
        self._pos_x += inc_x
        self._pos_y += inc_y

    def tree_here(self):
        char = self._data[self._pos_y][self._pos_x % self._width]
        return char == "#"

    def is_inside(self):
        return self._pos_y < self._height

    def home(self):
        self._pos_x = 0
        self._pos_y = 0

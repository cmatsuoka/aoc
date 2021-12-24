class Image:
    def __init__(self, data):
        self._data = data
        self._width = len(data[0])
        self._height = len(data)

    @classmethod
    def from_file(cls, input_file):
        data = [list(line.strip()) for line in input_file]
        return cls(data)

    def pad(self, size, char):
        data = []
        for _ in range(size):
            data.append([char] * (self._width + 2 * size))
        for row_data in self._data:
            data.append([char] * size + row_data + [char] * size)
        for _ in range(size):
            data.append([char] * (self._width + 2 * size))
        self._data = data
        self._width += 2 * size
        self._height += 2 * size

    def dump(self):
        for row_data in self._data:
            print("".join(row_data))
        print()

    def enhance(self, algo, odd):
        pad_char = algo[0] if odd else "."

        data = []
        for _ in range(self._height):
            data.append([pad_char] * self._width)
        for i in range(1, self._height - 1):
            for j in range(1, self._width - 1):
                data[i][j] = self._enhance_char(i, j, algo)
        self._data = data

    def _enhance_char(self, row, column, algo):
        idx = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                idx <<= 1
                if self._data[row + i][column + j] != ".":
                    idx |= 1
        return algo[idx]

    def count(self):
        num = 0
        for row_data in self._data:
            num += row_data.count("#")
        return num

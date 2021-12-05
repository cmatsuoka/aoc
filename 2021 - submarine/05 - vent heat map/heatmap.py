class Heatmap:
    def __init__(self, width: int, height: int):
        data = []
        for j in range(height):
            data.append([0] * width)
        self._width = width
        self._height = height
        self._data = data

    def __repr__(self):
        res = []
        for row in self._data:
            res.append(format("".join([chr(x + ord("0")) for x in row])))
        return "\n".join(res).replace("0", ".")

    def add(self, x: int, y: int) -> None:
        if x >= self._width or y >= self._height:
            raise ValueError(f"invalid coordinates {x},{y}")
        self._data[y][x] += 1

    def count(self, min_value: int) -> int:
        num = 0
        for row in self._data:
            for val in row:
                if val >= min_value:
                    num += 1
        return num

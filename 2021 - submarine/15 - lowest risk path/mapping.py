from heapq import heappush, heappop


_MAX_COST = (1 << 32) - 1


class RiskMap:
    def __init__(self, data):
        self._data = data
        self._width = len(data[0])
        self._height = len(data)
        self._visited = [[False] * self._width for _ in range(self._height)]
        self._cost = [[_MAX_COST] * self._width for _ in range(self._height)]
        self._queue = []

    @classmethod
    def from_file(cls, input_file):
        data = []
        for line in input_file:
            data.append([int(x) for x in line.strip()])
        return cls(data)

    def dijkstra(self):
        x = y = 0
        self._cost[y][x] = 0
        self._visited[y][x] = True
        self._update_cost(x, y)

        while self._queue:
            _, x, y = heappop(self._queue)
            self._update_cost(x, y)

        return self._cost[self._height - 1][self._width - 1]

    def _update_cost(self, x0, y0):
        cost0 = self._cost[y0][x0]

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            x, y = x0 + dx, y0 + dy
            if x < 0 or x >= self._width or y < 0 or y >= self._height:
                continue

            cost = cost0 + self._data[y][x]
            if not self._visited[y][x]:
                heappush(self._queue, (cost, x, y))
                self._visited[y][x] = True

            if cost < self._cost[y][x]:
                self._cost[y][x] = cost

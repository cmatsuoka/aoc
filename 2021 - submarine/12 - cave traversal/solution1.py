import fileinput


class Cave:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def is_major(self):
        return self.name[0].isupper()

    def is_end(self):
        return self.name == "end"


class Caves:
    def __init__(self):
        self.by_name = {"start": Cave("start")}
        self.solutions = 0

    def add(self, n1, n2):
        cave1 = self.by_name.get(n1)
        if not cave1:
            cave1 = Cave(n1)
            self.by_name[n1] = cave1

        cave2 = self.by_name.get(n2)
        if not cave2:
            cave2 = Cave(n2)
            self.by_name[n2] = cave2

        cave1.connections.append(cave2)
        cave2.connections.append(cave1)

    def traverse(self, cave, visits):
        if not cave.is_major() and cave.name in visits:
            return

        visits.add(cave.name)

        for conn in cave.connections:
            if conn.is_end():
                self.solutions += 1
            else:
                self.traverse(conn, visits.copy())


def solve(input_file):
    caves = Caves()
    for line in input_file:
        nodes = line.strip().split("-")
        caves.add(*nodes)

    caves.traverse(caves.by_name["start"], set())
    return caves.solutions


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

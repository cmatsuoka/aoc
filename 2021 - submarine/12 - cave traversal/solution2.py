import fileinput


class Cave:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.max_visits = 1  # visits for minor caves

    def is_major(self):
        return self.name[0].isupper()

    def is_start(self):
        return self.name == "start"

    def is_end(self):
        return self.name == "end"


class Caves:
    def __init__(self):
        self.by_name = {"start": Cave("start")}
        self.minor_list = []  # all minor caves except start and end
        self.solutions = set()

    def add(self, n1, n2):
        cave1 = self.by_name.get(n1)
        if not cave1:
            cave1 = Cave(n1)
            self.by_name[n1] = cave1
            if not cave1.is_major():
                self.minor_list.append(cave1)

        cave2 = self.by_name.get(n2)
        if not cave2:
            cave2 = Cave(n2)
            self.by_name[n2] = cave2
            if not cave2.is_major():
                self.minor_list.append(cave2)

        cave1.connections.append(cave2)
        cave2.connections.append(cave1)

    def traverse(self, cave, visits, path):
        if cave.is_end():
            self.solutions.add(path)
            return

        if (
            not cave.is_major()
            and visits.get(cave.name)
            and visits[cave.name] >= cave.max_visits
        ):
            return

        if cave.name in visits:
            visits[cave.name] += 1
        else:
            visits[cave.name] = 1

        for conn in cave.connections:
            self.traverse(conn, visits.copy(), f"{path}-{conn.name}")


def solve(input_file):
    caves = Caves()
    for line in input_file:
        nodes = line.strip().split("-")
        caves.add(*nodes)

    for minor_cave in caves.minor_list:
        minor_cave.max_visits = 2
        caves.traverse(caves.by_name["start"], {}, "start")
        minor_cave.max_visits = 1

    return len(caves.solutions)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

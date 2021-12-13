import re
from collections import namedtuple


Dot = namedtuple("Dot", ["x", "y"])
Fold = namedtuple("Fold", ["where", "vertical"])


class Origami:
    def __init__(self, dots, instructions):
        self._dots = dots
        self._instructions = instructions
        self._ip = 0
        self._height = max([dot.y for dot in self._dots]) + 1
        self._width = max([dot.x for dot in self._dots]) + 1

    @classmethod
    def from_file(cls, input_file):
        dots = set()
        for line in input_file:
            if line == "\n":
                break
            x, y = line.split(",")
            dots.add(Dot(int(x), int(y)))

        instructions = []
        for line in input_file:
            m = re.match(r"fold along ([xy])=([0-9]+)", line)
            instructions.append(Fold(int(m.group(2)), m.group(1) == "x"))

        return cls(dots, instructions)

    def fold(self):
        if self._ip >= len(self._instructions):
            return False

        inst = self._instructions[self._ip]
        print("FOLD:", inst)
        self._ip += 1

        new_dots = set()

        if inst.vertical:
            for dot in self._dots:
                if dot.x > inst.where:
                    new_x = inst.where + inst.where - dot.x
                    new_dots.add(Dot(new_x, dot.y))
                else:
                    new_dots.add(dot)
            self._width = inst.where
        else:
            for dot in self._dots:
                if dot.y > inst.where:
                    new_y = inst.where + inst.where - dot.y
                    new_dots.add(Dot(dot.x, new_y))
                else:
                    new_dots.add(dot)
            self._height = inst.where

        self._dots = new_dots

        return True

    def count_dots(self):
        return len(self._dots)

    def content(self):
        paper = []
        for i in range(self._height):
            paper.append(list("." * self._width))

        for dot in self._dots:
            paper[dot.y][dot.x] = "#"

        return ["".join(line) for line in paper]

import fileinput
from functools import reduce
from typing import List


class _MonkeyNote:
    def __init__(self, input_file: fileinput.FileInput) -> None:
        self.starting_items = [int(x) for x in input_file.readline()[18:].split(",")]
        (self.operator, self.operand) = input_file.readline().split()[-2:]
        self.divisible_by = int(input_file.readline().split()[-1])
        self.throw_true = int(input_file.readline().split()[-1])
        self.throw_false = int(input_file.readline().split()[-1])


def solve(input_file: fileinput.FileInput) -> int:
    notes: List[_MonkeyNote] = []
    while True:
        # Read notes from input file
        line = input_file.readline().strip()
        assert line.startswith("Monkey ")
        notes.append(_MonkeyNote(input_file))
        line = input_file.readline()
        if not line:
            break

    # Set the modulus to the product of all monkey test divisors
    modulus = reduce(lambda x, y: x * y, [n.divisible_by for n in notes])

    # Each monkey starts with list of items
    monkey_items = [n.starting_items for n in notes]

    # Each monkey has an activity level
    monkey_activity = [0] * len(notes)

    # Execute the simulation
    for _ in range(10000):
        for monkey, note in enumerate(notes):
            num_items = len(monkey_items[monkey])
            monkey_activity[monkey] += num_items
            for _ in range(num_items):
                item = monkey_items[monkey].pop(0)  # get item to examine
                operand = item if note.operand == "old" else int(note.operand)
                worry_level = item + operand if note.operator == "+" else item * operand
                worry_level %= modulus  # new worry reducing operation
                if worry_level % note.divisible_by:
                    monkey_items[note.throw_false].append(worry_level)
                else:
                    monkey_items[note.throw_true].append(worry_level)

    monkey_activity.sort(reverse=True)
    return monkey_activity[0] * monkey_activity[1]


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

import fileinput
import re
from dataclasses import dataclass


@dataclass
class Bags:
    num: int
    color: str


def _count_bags(target, rules):
    """Recursively get number of bags inside target."""
    num = 0
    for bag in rules[target]:
        if bag.num:
            num += bag.num + bag.num * _count_bags(bag.color, rules)

    return num


def solve(input_file):
    bag_rules = {}

    for line in input_file:
        line = line.strip()
        container, content_list = line.split(" bags contain ")

        content = []
        for x in content_list.split(", "):
            match = re.match(r"([0-9]+ )?(.*) bags?\.?", x)
            num = int(match.group(1)) if match.group(1) else 0
            content.append(Bags(num, match.group(2)))

        bag_rules[container] = content

    return _count_bags("shiny gold", bag_rules)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

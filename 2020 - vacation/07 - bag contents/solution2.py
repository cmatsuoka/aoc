import fileinput
import re
from dataclasses import dataclass


@dataclass
class Bags:
    num: int
    color: str


def count_bags(target, rules):
    """Recursively get number of bags inside target."""
    num = 0
    for bag in rules[target]:
        if bag.num:
            num += bag.num + bag.num * count_bags(bag.color, rules)

    return num

bag_rules = {}

for line in fileinput.input():
    line = line.strip()
    container, content_list = line.split(" bags contain ")

    content = []
    for x in content_list.split(", "):
        match = re.match(r"([0-9]+ )?(.*) bags?\.?", x)
        num = int(match.group(1)) if match.group(1) else 0
        content.append(Bags(num, match.group(2)))

    bag_rules[container] = content

total = count_bags("shiny gold", bag_rules)

print(total)

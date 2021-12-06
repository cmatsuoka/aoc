import fileinput
import re
from dataclasses import dataclass


@dataclass
class Bags:
    num: int
    color: str


def _build_container_map(rules):
    """Map each color to a list of possible parents."""
    container_map = {}
    for container, content_list in rules.items():
        for content in content_list:
            container_map.setdefault(content.color, [])
            container_map[content.color].append(container)

    return container_map


def _get_container_set(target, container_map):
    """Recursively obtain the set of parents for a target color."""
    if target not in container_map:
        return set()

    containers = set(container_map[target])

    for container in containers.copy():
        containers |= _get_container_set(container, container_map)

    return containers


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

    container_map = _build_container_map(bag_rules)

    container_set = _get_container_set("shiny gold", container_map)

    return len(container_set)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

class Polymerizer:
    def __init__(self, rules, template):
        self._rules = rules

        # set up element table
        elements = {}
        for e in template:
            _insert(elements, e)
        self._elements = elements

        # set up pair table
        pairs = {}
        for i in range(len(template) - 1):
            pair = template[i : i + 2]
            _insert(pairs, pair, 1)
        self._pairs = pairs

    @classmethod
    def from_file(cls, input_file):
        template = input_file.readline().strip()
        input_file.readline()

        rules = {}
        for line in input_file:
            r = line.strip().split(" -> ")
            rules[r[0]] = r[1]

        return cls(rules, template)

    def run(self):
        new_pairs = {}
        for pair, num in self._pairs.items():
            if pair in self._rules:
                elem = self._rules[pair]
                _insert(new_pairs, pair[0] + elem, num)
                _insert(new_pairs, elem + pair[1], num)
                _insert(self._elements, elem, num)
        self._pairs = new_pairs

    def get_element_count(self):
        return min(self._elements.values()), max(self._elements.values())


def _insert(table, item, num=1):
    table[item] = table.get(item, 0) + num

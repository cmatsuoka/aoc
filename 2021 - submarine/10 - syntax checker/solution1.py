import fileinput


_PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


class Stack(list):
    push = list.append


def solve(input_file):
    points = 0
    for line in input_file:
        # incomplete lines will return 0
        points += _check_syntax(list(line.strip()))
    return points


def _check_syntax(symbol_list):
    stack = Stack()
    for i in range(len(symbol_list)):
        char = symbol_list.pop(0)
        if char in _PAIRS:
            stack.push(_PAIRS[char])
        else:
            expected = stack.pop()
            if char != expected:
                # syntax error
                return _POINTS[char]
    return 0


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

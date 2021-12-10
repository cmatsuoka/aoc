import fileinput


_PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


class Stack(list):
    push = list.append


def solve(input_file):
    score_list = []
    for line in input_file:
        # corrupt lines will return None
        stack = _check_syntax(list(line.strip()))

        # skip corrupted lines
        if not stack:
            continue

        # get missing characters from stack and compute points
        points = 0
        while stack:
            char = stack.pop()
            points *= 5
            points += _POINTS[char]
        score_list.append(points)

    score_list.sort()
    return score_list[int(len(score_list) / 2)]


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
                return None
    return stack


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

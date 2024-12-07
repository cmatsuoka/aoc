import fileinput
import itertools


def operators(n: int) -> itertools.product:
    ops = [("+", "*")] * n
    return itertools.product(*ops)


def evaluate(operands: list[int], operators: tuple[str, ...]) -> int:
    res = operands.pop(0)
    for n in range(len(operators)):
        op = operators[n]
        if op == "+":
            res = res + operands[n]
        elif op == "*":
            res = res * operands[n]
        else:
            raise ValueError
    return res


def solve(input_file: fileinput.FileInput[str]) -> int:
    eqs: list[list[int]] = []
    for line in input_file:
        line = line.replace(":", " ")
        eqs.append([int(x) for x in line.strip().split()])

    total = 0
    for eq in eqs:
        ops = operators(len(eq) - 2)
        for op in ops:
            val = int(eq[0])
            if evaluate(eq[1:], op) == val:
                total += val
                break

    return total


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

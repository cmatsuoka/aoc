import fileinput

import solution1
import solution2


def test_solution1_example():
    file_input = fileinput.FileInput("test_data.txt")

    assert solution1.solve(file_input) == 18


def test_solution1():
    file_input = fileinput.FileInput("input.txt")
    assert solution1.solve(file_input) == 2545


def test_solution2_example():
    file_input = fileinput.FileInput("test_data.txt")
    assert solution2.solve(file_input) == 9


def test_solution2():
    file_input = fileinput.FileInput("input.txt")
    assert solution2.solve(file_input) == 1886

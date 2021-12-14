import fileinput

import solution1
import solution2


def test_solution1_example():
    file_input = fileinput.FileInput("test_data.txt")
    assert solution1.solve(file_input, 10) == 1588


def test_solution1():
    file_input = fileinput.FileInput("input.txt")
    assert solution1.solve(file_input, 10) == 2988


def test_solution2_example():
    file_input = fileinput.FileInput("test_data.txt")
    assert solution2.solve(file_input, 40) == 2188189693529


def test_solution2():
    file_input = fileinput.FileInput("input.txt")
    assert solution2.solve(file_input, 40) == 3572761917024

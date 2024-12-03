import fileinput

import solution1
import solution2


def test_solution1_example():
    file_input = fileinput.FileInput("test_data_1.txt")
    assert solution1.solve(file_input) == 161


def test_solution1():
    file_input = fileinput.FileInput("input.txt")
    assert solution1.solve(file_input) == 175700056


def test_solution2_example():
    file_input = fileinput.FileInput("test_data_2.txt")
    assert solution2.solve(file_input) == 48


def test_solution2():
    file_input = fileinput.FileInput("input.txt")
    assert solution2.solve(file_input) == 71668682

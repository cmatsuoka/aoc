import fileinput

import solution1
import solution2


def test_solution1_example():
    file_input = fileinput.FileInput("test_data.txt")
    assert solution1.solve(file_input) == 26

def test_solution1():
    file_input = fileinput.FileInput("input.txt")
    assert solution1.solve(file_input) == 514

def test_solution2_example():
    file_input = fileinput.FileInput("test_data.txt")
    assert solution2.solve(file_input) == 61229

def test_solution2():
    file_input = fileinput.FileInput("input.txt")
    assert solution2.solve(file_input) == 1012272

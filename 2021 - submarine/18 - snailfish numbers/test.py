import fileinput

import solution1
import solution2


def test_solution1_example():
    file_input = fileinput.FileInput("test_data.txt")
    assert solution1.solve(file_input) == 3488


def test_solution1_example_2():
    file_input = fileinput.FileInput("test_data_2.txt")
    assert solution1.solve(file_input) == 4140


def test_solution1():
    file_input = fileinput.FileInput("input.txt")
    assert solution1.solve(file_input) == 4433


def test_solution2_example_2():
    file_input = fileinput.FileInput("test_data_2.txt")
    assert solution2.solve(file_input) == 3993


def test_solution2():
    file_input = fileinput.FileInput("input.txt")
    assert solution2.solve(file_input) == 4559

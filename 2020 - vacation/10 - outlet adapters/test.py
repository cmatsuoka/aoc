import fileinput

import solution1
import solution2


def test_solution1_example():
    file_input = fileinput.FileInput("test_data.txt")
    assert solution1.solve(file_input) == 35


def test_solution1_example_2():
    file_input = fileinput.FileInput("test_data_2.txt")
    assert solution1.solve(file_input) == 220


def test_solution1():
    file_input = fileinput.FileInput("input.txt")
    assert solution1.solve(file_input) == 2760


def test_solution2_example():
    file_input = fileinput.FileInput("test_data.txt")
    assert solution2.solve(file_input) == 8


def test_solution2_example_2():
    file_input = fileinput.FileInput("test_data_2.txt")
    assert solution2.solve(file_input) == 19208


def test_solution2():
    file_input = fileinput.FileInput("input.txt")
    assert solution2.solve(file_input) == 13816758796288

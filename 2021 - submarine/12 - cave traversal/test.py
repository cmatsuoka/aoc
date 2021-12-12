import fileinput

import solution1
import solution2


def test_solution1_example():
    file_input = fileinput.FileInput("test_data.txt")
    assert solution1.solve(file_input) == 10


def test_solution1_example_2():
    file_input = fileinput.FileInput("test_data_2.txt")
    assert solution1.solve(file_input) == 19


def test_solution1_example_3():
    file_input = fileinput.FileInput("test_data_3.txt")
    assert solution1.solve(file_input) == 226


def test_solution1():
    file_input = fileinput.FileInput("input.txt")
    assert solution1.solve(file_input) == 4241


def test_solution2_example():
    file_input = fileinput.FileInput("test_data.txt")
    assert solution2.solve(file_input) == 36


def test_solution2_example_2():
    file_input = fileinput.FileInput("test_data_2.txt")
    assert solution2.solve(file_input) == 103


def test_solution2_example_3():
    file_input = fileinput.FileInput("test_data_3.txt")
    assert solution2.solve(file_input) == 3509


def test_solution2():
    file_input = fileinput.FileInput("input.txt")
    assert solution2.solve(file_input) == 122134

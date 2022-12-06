import fileinput
import pytest

import solution1
import solution2


@pytest.mark.parametrize(
    "filename,count",
    [
        ("test_data0.txt", 7),
        ("test_data1.txt", 5),
        ("test_data2.txt", 6),
        ("test_data3.txt", 10),
        ("test_data4.txt", 11),
    ],
)
def test_solution1_example(filename: str, count: int):
    file_input = fileinput.FileInput(filename)
    assert solution1.solve(file_input) == count


def test_solution1():
    file_input = fileinput.FileInput("input.txt")
    assert solution1.solve(file_input) == 1833


@pytest.mark.parametrize(
    "filename,count",
    [
        ("test_data0.txt", 19),
        ("test_data1.txt", 23),
        ("test_data2.txt", 23),
        ("test_data3.txt", 29),
        ("test_data4.txt", 26),
    ],
)
def test_solution2_example(filename: str, count: int):
    file_input = fileinput.FileInput(filename)
    assert solution2.solve(file_input) == count


def test_solution2():
    file_input = fileinput.FileInput("input.txt")
    assert solution2.solve(file_input) == 3425

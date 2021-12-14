import fileinput

import pytest

import solution1
import solution2


@pytest.mark.parametrize(
    "starting,number",
    [
        ([0, 3, 6], 436),
        ([1, 3, 2], 1),
        ([2, 1, 3], 10),
        ([1, 2, 3], 27),
        ([2, 3, 1], 78),
        ([3, 2, 1], 438),
        ([3, 1, 2], 1836),
    ],
)
def test_solution1_example(starting, number):
    assert solution1.solve(starting, 2020) == number


def test_solution1():
    assert solution1.solve([2, 1, 10, 11, 0, 6], 2020) == 232


@pytest.mark.parametrize(
    "starting,number",
    [
        ([0, 3, 6], 175594),
        ([1, 3, 2], 2578),
        ([2, 1, 3], 3544142),
        ([1, 2, 3], 261214),
        ([2, 3, 1], 6895259),
        ([3, 2, 1], 18),
        ([3, 1, 2], 362),
    ],
)
def test_solution2_example(starting, number):
    assert solution2.solve(starting, 30000000) == number


def test_solution2():
    assert solution2.solve([2, 1, 10, 11, 0, 6], 30000000) == 18929178

import fileinput

import pytest

import solution1
import solution2


@pytest.mark.parametrize(
    "s,versum",
    [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_solution1_example(s, versum):
    assert solution1.solve_from_string(s) == versum


def test_solution1():
    file_input = fileinput.FileInput("input.txt")
    assert solution1.solve(file_input) == 897


@pytest.mark.parametrize(
    "s,result",
    [
        # find the sum of 1 and 2
        ("C200B40A82", 3),
        # find the product of 6 and 9
        ("04005AC33890", 54),
        # find the minimum of 7, 8, and 9
        ("880086C3E88112", 7),
        # find the maximum of 7, 8, and 9
        ("CE00C43D881120", 9),
        # verify if 5 is less than 15
        ("D8005AC2A8F0", 1),
        # verify if 5 is greater than 15
        ("F600BC2D8F", 0),
        # verify if 5 is equal to 15
        ("9C005AC2F8F0", 0),
        # verify if 1 + 3 = 2 * 2
        ("9C0141080250320F1802104A08", 1),
    ],
)
def test_solution2_example(s, result):
    assert solution2.solve_from_string(s) == result


def test_solution2():
    file_input = fileinput.FileInput("input.txt")
    assert solution2.solve(file_input) == 9485076995911

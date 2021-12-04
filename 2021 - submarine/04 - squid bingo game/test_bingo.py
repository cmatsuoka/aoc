
import pytest

import bingo


def test_extract_lines():
    lines = bingo._extract_lines(4, 4, list(range(16)))
    assert lines == [
       { 0, 1, 2, 3 },
       { 4, 5, 6, 7 },
       { 8, 9, 10, 11 },
       { 12, 13, 14, 15 },
    ]


def test_extract_lines_error():
    with pytest.raises(ValueError) as raised:
        lines = bingo._extract_lines(4, 4, list(range(15)))
    assert str(raised.value) == "board size and data are inconsistent"


def test_extract_columns():
    columns = bingo._extract_columns(4, 4, list(range(16)))
    assert columns == [
       { 0, 4, 8, 12 },
       { 1, 5, 9, 13 },
       { 2, 6, 10, 14 },
       { 3, 7, 11, 15 },
    ]


def test_extract_columns_error():
    with pytest.raises(ValueError) as raised:
        lines = bingo._extract_columns(4, 4, list(range(17)))
    assert str(raised.value) == "board size and data are inconsistent"


def test_board():
    board = bingo.Board(3, 3, list(range(9)))
    assert board._lines == [
        { 0, 1, 2 },
        { 3, 4, 5 },
        { 6, 7, 8 },
    ]
    assert board._columns == [
        { 0, 3, 6 },
        { 1, 4, 7 },
        { 2, 5, 8 },
    ]
 

def test_mark_number():
    board = bingo.Board(4, 4, list(range(16)))
    board.mark_number(9)
    assert board._lines == [
       { 0, 1, 2, 3 },
       { 4, 5, 6, 7 },
       { 8, 10, 11 },
       { 12, 13, 14, 15 },
    ]
    assert board._columns == [
       { 0, 4, 8, 12 },
       { 1, 5, 13 },
       { 2, 6, 10, 14 },
       { 3, 7, 11, 15 },
    ]


def test_mark_number_bingo():
    board = bingo.Board(3, 3, list(range(9)))
    board.mark_number(7)
    board.mark_number(6)

    with pytest.raises(bingo.Bingo) as raised:
        board.mark_number(8)
    assert str(raised.value) == "Bingo!"


def test_sum_remaining():
    board = bingo.Board(4, 4, list(range(16)))
    board.mark_number(9)
    board.mark_number(2)
    assert board.sum_remaining() == 109

import pytest
import common


@pytest.mark.parametrize(
    "data,start,end",
    [
        ("0-0", 0, 0),
        ("11-22", 11, 22),
    ],
)
def test_parse(data: str, start: int, end: int):
    assert common.SectionRange.parse(data) == common.SectionRange(start, end)


@pytest.mark.parametrize(
    "range1,range2,res",
    [
        ("1-2", "3-4", False),
        ("1-2", "2-3", False),
        ("1-2", "2-2", True),
        ("1-3", "2-2", True),
        ("2-2", "2-2", True),
        ("2-3", "2-2", True),
        ("2-3", "1-2", False),
        ("2-3", "1-1", False),
    ],
)
def test_contains(range1: str, range2: str, res: bool):
    sr1 = common.SectionRange.parse(range1)
    sr2 = common.SectionRange.parse(range2)
    assert sr1.contains(sr2) == res


@pytest.mark.parametrize(
    "range1,range2,res",
    [
        ("1-2", "3-4", False),
        ("1-2", "2-3", True),
        ("1-2", "2-2", True),
        ("1-3", "2-2", True),
        ("2-2", "2-2", True),
        ("2-3", "2-2", True),
        ("2-3", "1-2", True),
        ("2-3", "1-1", False),
    ],
)
def test_overlaps(range1: str, range2: str, res: bool):
    sr1 = common.SectionRange.parse(range1)
    sr2 = common.SectionRange.parse(range2)
    assert sr1.overlaps(sr2) == res

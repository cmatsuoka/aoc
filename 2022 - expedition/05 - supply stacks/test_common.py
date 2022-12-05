import fileinput
import pytest
from pathlib import Path
from typing import Dict, List

import common


@pytest.mark.parametrize(
    "lines,stacks",
    [
        ("[A]\n", {1: [65]}),
        ("    [A]\n", {2: [65]}),
        ("    [A]\n[B] [C]\n", {1: [66], 2: [67, 65]}),
    ],
)
def test_parse(lines: str, stacks: Dict[int, List[int]], tmpdir):
    test_file = Path(tmpdir / "test.txt")
    test_file.write_text(lines)
    cargo = common.Cargo()
    cargo.parse(fileinput.FileInput(test_file))
    assert cargo.stacks == stacks


@pytest.mark.parametrize(
    "num,src,dest,stacks0,stacks",
    [
        (0, 1, 2, {1: [65], 2: [66]}, {1: [65], 2: [66]}),
        (1, 1, 2, {1: [65], 2: [66]}, {1: [], 2: [66, 65]}),
        (1, 1, 2, {1: [65, 66], 2: [67]}, {1: [65], 2: [67, 66]}),
        (2, 1, 2, {1: [65, 66], 2: [67]}, {1: [], 2: [67, 66, 65]}),
    ],
)
def test_move(
    num: int,
    src: int,
    dest: int,
    stacks0: Dict[int, List[int]],
    stacks: Dict[int, List[int]],
):
    cargo = common.Cargo(stacks=stacks0)
    cargo.move(num, src, dest)
    assert cargo.stacks == stacks


@pytest.mark.parametrize(
    "num,src,dest,stacks0,stacks",
    [
        (0, 1, 2, {1: [65], 2: [66]}, {1: [65], 2: [66]}),
        (1, 1, 2, {1: [65], 2: [66]}, {1: [], 2: [66, 65]}),
        (1, 1, 2, {1: [65, 66], 2: [67]}, {1: [65], 2: [67, 66]}),
        (2, 1, 2, {1: [65, 66], 2: [67]}, {1: [], 2: [67, 65, 66]}),
    ],
)
def test_move_multiple(
    num: int,
    src: int,
    dest: int,
    stacks0: Dict[int, List[int]],
    stacks: Dict[int, List[int]],
):
    cargo = common.Cargo(stacks=stacks0)
    cargo.move(num, src, dest, multiple=True)
    assert cargo.stacks == stacks


@pytest.mark.parametrize(
    "stacks,res",
    [
        ({1: [65]}, "A"),
        ({1: [65], 2: [66]}, "AB"),
        ({1: [65, 66], 2: [67]}, "BC"),
    ],
)
def test_top_crates(stacks: Dict[int, List[int]], res: str):
    cargo = common.Cargo(stacks=stacks)
    assert cargo.top_crates() == res

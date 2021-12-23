import pytest

import number
from number import Node, Number


@pytest.mark.parametrize(
    "num,parts",
    [
        ("[1,2]", ("1", "2")),
        ("[1,[2,3]]", ("1", "[2,3]")),
        ("[[1,2],3]", ("[1,2]", "3")),
        ("[[1,2],[3,4]]", ("[1,2]", "[3,4]")),
        ("[[1,[2,34]],[[56,7],8]]", ("[1,[2,34]]", "[[56,7],8]")),
    ],
)
def test_extract(num, parts):
    assert number.extract(num) == parts


@pytest.mark.parametrize(
    "num,tree",
    [
        ("[1,2]", Node(left=Node(1, depth=2), right=Node(2, depth=2), depth=1)),
        (
            "[1,[2,3]]",
            Node(
                left=Node(1, depth=2),
                right=Node(left=Node(2, depth=3), right=Node(3, depth=3), depth=2),
                depth=1,
            ),
        ),
        (
            "[[1,2],3]",
            Node(
                left=Node(left=Node(1, depth=3), right=Node(2, depth=3), depth=2),
                right=Node(3, depth=2),
                depth=1,
            ),
        ),
        (
            "[[1,2],[3,4]]",
            Node(
                left=Node(left=Node(1, depth=3), right=Node(2, depth=3), depth=2),
                right=Node(left=Node(3, depth=3), right=Node(4, depth=3), depth=2),
                depth=1,
            ),
        ),
        (
            "[[1,[2,34]],[[56,7],8]]",
            Node(
                left=Node(
                    left=Node(1, depth=3),
                    right=Node(left=Node(2, depth=4), right=Node(34, depth=4), depth=3),
                    depth=2,
                ),
                right=Node(
                    left=Node(left=Node(56, depth=4), right=Node(7, depth=4), depth=3),
                    right=Node(8, depth=3),
                    depth=2,
                ),
                depth=1,
            ),
        ),
    ],
)
def test_build_tree(num, tree):
    assert number._build_tree(num) == tree


@pytest.mark.parametrize(
    "num",
    [
        "[1,2]",
        "[1,[2,3]]",
        "[[1,2],3]",
        "[[1,2],[3,4]]",
        "[[1,[2,34]],[[56,7],8]]",
    ],
)
def test_repr(num):
    tree = number._build_tree(num)
    assert repr(tree) == num


@pytest.mark.parametrize(
    "num,res",
    [
        ("[1,2]", "[1,2]"),
        ("[1,[2,3]]", "[1,[2,3]]"),
        ("[10,11]", "[[5,5],11]"),
        ("[[5,5],11]", "[[5,5],[5,6]]"),
    ],
)
def test_split(num, res):
    n = Number.parse(num)
    n.split()
    assert repr(n) == res


@pytest.mark.parametrize(
    "num,res",
    [
        ("[1,2]", "[1,2]"),
        ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
        ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
        ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
        ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
        ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
    ],
)
def test_explode(num, res):
    n = Number.parse(num)
    n.explode()
    assert repr(n) == res


@pytest.mark.parametrize(
    "nums,res",
    [
        (("[1,2]", "[[3,4],5]"), "[[1,2],[[3,4],5]]"),
        (
            ("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]"),
            "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]",
        ),
        (
            (
                "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
                "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
            ),
            "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]",
        ),
    ],
)
def test_add(nums, res):
    a = Number.parse(nums[0])
    for num in nums[1:]:
        a += Number.parse(num)
    assert repr(a) == res


@pytest.mark.parametrize(
    "num,res",
    [
        ("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]", "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"),
    ],
)
def test_reduce(num, res):
    n = Number.parse(num)
    n.reduce()
    assert repr(n) == res


@pytest.mark.parametrize(
    "num,res",
    [
        ("[[1,2],[[3,4],5]]", 143),
        ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
        ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
        ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
        ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
        ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
    ],
)
def test_magnitude(num, res):
    n = Number.parse(num)
    assert n.magnitude == res

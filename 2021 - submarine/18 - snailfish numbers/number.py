import copy
import fileinput
import math
from typing import List


class StopSearch(Exception):
    pass


class Node:
    def __init__(self, val=None, left=None, right=None, depth=0):
        self.val = val
        self.left = left
        self.right = right
        self.depth = depth

    def __eq__(self, other):
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
            and self.depth == other.depth
        )

    def __repr__(self):
        if self.val is not None:
            return str(self.val)
        return f"[{self.left},{self.right}]"

    def is_leaf(self):
        return self.val is not None


class Number:
    def __init__(self, root: Node):
        self._root = root
        self._last_node = None  # node with previous leaf
        self._add_rval = None  # value to add to next leaf

    def __repr__(self):
        return repr(self._root)

    def __add__(self, other):
        n = self.__class__(
            Node(left=copy.deepcopy(self.tree), right=copy.deepcopy(other.tree))
        )
        _add_depth(n._root)
        return n.reduce()

    @classmethod
    def parse(cls, num: str):
        node = _build_tree(num)
        return cls(node)

    @property
    def tree(self) -> Node:
        return self._root

    @property
    def magnitude(self) -> int:
        return self._mag_search(self._root)

    def _mag_search(self, node):
        if node.is_leaf():
            return node.val
        return 3 * self._mag_search(node.left) + 2 * self._mag_search(node.right)

    def split(self):
        try:
            self._split_search(self._root)
        except StopSearch:
            pass

    def _split_search(self, node):
        if node.is_leaf():
            val = node.val
            if val >= 10:
                node.val = None
                node.left = Node(math.floor(val / 2), depth=node.depth + 1)
                node.right = Node(math.ceil(val / 2), depth=node.depth + 1)
                raise StopSearch(node)
        else:
            self._split_search(node.left)
            self._split_search(node.right)

    def explode(self):
        self._last_node = None
        self._add_rval = None
        try:
            self._explode_search(self._root)
        except StopSearch:
            pass

    def _explode_search(self, node):
        if node.is_leaf():
            if self._add_rval:
                node.val += self._add_rval
                raise StopSearch(node)

            self._last_node = node
            return

        if (
            node.left.is_leaf()
            and node.right.is_leaf()
            and node.depth > 4
            and self._add_rval is None
        ):
            lval = node.left.val
            rval = node.right.val
            node.val = 0
            node.left = None
            node.right = None

            if self._last_node:
                self._last_node.val += lval

            self._add_rval = rval
        else:
            self._explode_search(node.left)
            self._explode_search(node.right)

    def reduce(self) -> "Number":
        while True:
            prev = repr(self._root)
            while True:
                prev2 = repr(self._root)
                self.explode()
                if prev2 == repr(self._root):
                    break
            self.split()
            if prev == repr(self._root):
                break
        return self


def _build_tree(v: str, depth=0) -> Node:
    depth += 1
    try:
        return Node(int(v), depth=depth)  # leaf node with regular number
    except ValueError:
        pass

    node = Node(depth=depth)
    l, r = extract(v)

    node.left = _build_tree(l, depth)
    node.right = _build_tree(r, depth)

    return node


def _add_depth(node: Node):
    node.depth += 1
    if node.left:
        _add_depth(node.left)
    if node.right:
        _add_depth(node.right)


def _get_token(v: str):
    num = ""
    for c in v:
        if c in ("[", "]", ","):
            if num:
                yield num
                num = ""
            yield c

        elif c.isdigit():
            num += c


def extract(v: str) -> str:
    level = 0
    pos = 0
    for t in _get_token(v):
        if t == "[":
            level += 1
            pos += 1
            if level == 1:
                start_l = pos
        elif t == ",":
            if level == 1:
                end_l = pos
                start_r = pos + 1
            pos += 1
        elif t == "]":
            if level == 1:
                end_r = pos
            pos += 1
            level -= 1
        else:
            pos += len(t)

    return v[start_l:end_l], v[start_r:end_r]

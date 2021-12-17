import fileinput

from bstream import Bitstream
from protocol import Parser


def solve(input_file):
    return _solve(Bitstream.from_file(input_file))


def solve_from_string(s):
    return _solve(Bitstream.from_string(s))


def _solve(bs):
    p = Parser(bs)
    p.read_packet()
    return p.versum


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

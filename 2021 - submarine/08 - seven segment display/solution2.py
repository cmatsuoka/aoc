import fileinput
import re


def solve(input_file):
    total = 0
    for line in input_file:
        parts = line.split(" | ")
        codes = parts[0].split()
        numbers = [set(x) for x in parts[1].split()]
        digits = _decode_segments(codes)

        value = 0
        for num in numbers:
            value *= 10
            value += digits.index(num)

        total += value

    return total


# segment layout:
#
#     aaaa
#    b    c
#    b    c
#     dddd
#    e    f
#    e    f
#     gggg
#
#
# sorted code example with mixed up segments:
#
#   0 ab: 1
#   1 dab: 7
#   2 eafb: 4
#   3 cdfbe: 5
#   4 gcdfa: 2
#   5 fbcad: 3
#   6 cefabd: 9
#   7 cdfgeb: 6
#   8 cagedb: 0
#   9 acedgfb: 8


def _decode_segments(codes):
    codes = sorted(codes, key=lambda x: len(x))
    codes = [set(x) for x in codes]

    seg_cf = codes[0]  # 1
    seg_acf = codes[1]  # 7
    seg_bcdf = codes[2]  # 4
    seg_all = codes[9]  # 8

    seg_a = seg_acf - seg_cf
    seg_bd = seg_bcdf - seg_cf
    seg_eg = seg_all - seg_a - seg_cf - seg_bd

    seg_cde = (seg_all - codes[6]) | (seg_all - codes[7]) | (seg_all - codes[8])
    seg_c = seg_acf.intersection(seg_cde)
    seg_de = seg_cde - seg_c
    seg_b = seg_bd - seg_de
    seg_d = seg_bd - seg_b
    seg_e = seg_cde - seg_c - seg_d
    seg_f = seg_cf - seg_c
    seg_g = seg_eg - seg_e

    return [
        seg_acf | seg_b | seg_eg,
        seg_cf,
        seg_a | seg_c | seg_d | seg_eg,
        seg_acf | seg_d | seg_g,
        seg_bcdf,
        seg_a | seg_bd | seg_f | seg_g,
        seg_a | seg_bd | seg_eg | seg_f,
        seg_acf,
        seg_all,
        seg_acf | seg_bd | seg_g,
    ]


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

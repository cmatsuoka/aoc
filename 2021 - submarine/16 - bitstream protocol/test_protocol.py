import protocol

import pytest


class TestBitstream:
    @pytest.mark.parametrize(
        "s,val",
        [
            ("", []),
            ("1", [0x10000000]),
            ("01", [0x01000000]),
            ("0102", [0x01020000]),
            ("0102030405", [0x01020304, 0x05000000]),
        ],
    )
    def test_from_string(self, s, val):
        bs = protocol.Bitstream.from_string(s)
        assert bs._data == val

    @pytest.mark.parametrize(
        "data,num,val",
        [
            ([], 0, 0),
            ([0xA0000000], 1, 1),
            ([0xA0000000], 2, 2),
            ([0x00000001], 32, 1),
            ([0x00000001, 0x80000000], 33, 3),
        ],
    )
    def test_get_bits(self, data, num, val):
        bs = protocol.Bitstream(data)
        assert bs.get_bits(num) == val

    @pytest.mark.parametrize(
        "data,num,val",
        [
            ([0x12340000], [2, 2, 4, 8], [0, 1, 2, 0x34]),
        ],
    )
    def test_get_bits_multiple(self, data, num, val):
        bs = protocol.Bitstream(data)
        for i in range(len(num)):
            assert bs.get_bits(num[i]) == val[i]


class TestProtocol:
    def test_read_packet(self):
        bs = protocol.Bitstream.from_string("D2FE28")
        p = protocol.Parser(bs)
        assert p.read_version() == 6
        assert p.read_type() == 4
        assert p.read_literal() == (2021, 15)

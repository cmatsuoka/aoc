from enum import Enum
from typing import Tuple

from bstream import Bitstream


class Operator(Enum):
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL_TO = 7

    def operate(self, v: int, u: int) -> int:
        if self is Operator.SUM:
            return v + u
        elif self is Operator.PRODUCT:
            return v * u
        elif self is Operator.MINIMUM:
            return v if v < u else u
        elif self is Operator.MAXIMUM:
            return v if v > u else u
        elif self is Operator.GREATER_THAN:
            return v > u
        elif self is Operator.LESS_THAN:
            return v < u
        elif self is Operator.EQUAL_TO:
            return v == u
        else:
            raise RuntimeError(f"unknown operation {self.value}")


class Parser:
    def __init__(self, bitstream: Bitstream):
        self._bitstream = bitstream
        self.versum = 0

    def read_packet(self) -> Tuple[int, int]:
        ver = self.read_version()
        typ = self.read_type()
        size = 6

        self.versum += ver

        if typ == 4:
            val, sz = self.read_literal()
            size += sz
        else:
            val, sz = self.read_operator(Operator(typ))
            size += sz

        return val, size

    def read_version(self) -> int:
        return self._bitstream.get_bits(3)

    def read_type(self) -> int:
        return self._bitstream.get_bits(3)

    def read_literal(self) -> Tuple[int, int]:
        val = size = 0
        while True:
            grp = self._bitstream.get_bits(5)
            size += 5
            val <<= 4
            val |= grp & 0x0F
            if grp & 0x10 == 0x00:
                break

        return val, size

    def read_operator(self, operator: Operator) -> Tuple[int, int]:
        lid = self._bitstream.get_bits(1)
        size = 1

        if lid == 0:
            # If the length type ID is 0, then the next 15 bits are a number that
            # represents the total length in bits of the sub-packets contained by this
            # packet.
            length = self._bitstream.get_bits(15)
            size += 15

            val, sz = self.read_packet()
            length -= sz
            size += sz

            while length > 0:
                next_val, sz = self.read_packet()
                length -= sz
                size += sz

                val = operator.operate(val, next_val)

            if length:
                raise RuntimeError("protocol error")
        else:
            # If the length type ID is 1, then the next 11 bits are a number that
            # represents the number of sub-packets immediately contained by this packet.
            numsub = self._bitstream.get_bits(11)
            size += 11

            val, sz = self.read_packet()
            size += sz

            for i in range(1, numsub):
                next_val, sz = self.read_packet()
                size += sz
                val = operator.operate(val, next_val)

        return val, size

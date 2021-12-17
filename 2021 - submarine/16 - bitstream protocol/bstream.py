from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from fileinput import FileInput


class Bitstream:
    def __init__(self, data: List[int]):
        self._data = data  # stored as a list of 32-bit words
        self._avail = 32  # bits available in data[0]

    @classmethod
    def from_string(cls, s: str) -> "Bitstream":
        if not s:
            return cls([])

        padding = 8 - (len(s) % 8)
        s += "0" * padding
        return cls([int(s[i : i + 8], 16) for i in range(0, len(s), 8)])

    @classmethod
    def from_file(cls, input_file: "FileInput") -> "Bitstream":
        line = input_file.readline()
        return cls.from_string(line.strip())

    def get_bits(self, num: int) -> int:
        val = 0
        for i in range(num):
            val <<= 1
            self._avail -= 1
            val |= (self._data[0] >> self._avail) & 1

            if not self._avail:
                self._data.pop(0)
                self._avail = 32

        return val

import io
import sys
from typing import List


class SignalProcessor:
    """Read characters from the input stream and detect protocol."""

    def __init__(self, input_file: io.TextIOWrapper, *, window_size: int) -> None:
        self._buffer: List[int] = [0] * window_size
        self._file = input_file
        self._window_size = window_size

        # fill buffer
        for i in range(window_size):
            self._buffer[i] = self._read_input()

    def detect_handshake(self) -> bool:
        """Read a character from input and check if protocol marker found."""
        val = self._read_input()
        self._buffer = self._buffer[1:] + [val]

        # not the most efficient but the easiest to implement
        return len(set(self._buffer)) == self._window_size

    def _read_input(self) -> int:
        """Read a character from input."""
        char = self._file.read(1)
        if not char:
            raise RuntimeError("protocol error")

        return ord(char)


def solve(file: io.TextIOWrapper) -> int:
    count = 14
    processor = common.SignalProcessor(file, window_size=count)

    while True:
        count += 1
        if processor.detect_handshake():
            return count


if __name__ == "__main__":
    # We could have slurped this as a single string but let's consider the
    # possibility of an infinite stream
    with open(sys.argv[1], encoding="ascii") as file:
        print(solve(file))

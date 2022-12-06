import fileinput


def _detect_handshake(data: bytes, window_size: int):
    for i in range(len(data)):
       if len(set(data[i:i+window_size])) == window_size:
           return i + window_size

    raise RuntimeError("protocol error")


def solve(input_file):
    data = bytes(input_file.readline().strip(), encoding="ascii")
    return _detect_handshake(data, 14)


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))

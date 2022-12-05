import fileinput
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Cargo:
    """Cargo hold with multiple crate stacks."""

    stacks: Dict[int, List[int]] = field(default_factory=lambda: defaultdict(list))

    def parse(self, input_file: fileinput.FileInput) -> None:
        """Read cargo contents from file."""
        for line in input_file:
            if "[" not in line:
                break

            for i in range(len(line) // 4):
                crate = ord(line[i * 4 + 1])  # int is faster than string
                if crate > 32:
                    self.stacks[i + 1].insert(0, crate)

    def move(self, num: int, src: int, dest: int, *, multiple: bool = False) -> None:
        """Move crates from a stack to another."""
        if num == 0:
            return

        src_crates = self.stacks[src][-num:]
        if not multiple:
            src_crates.reverse()

        self.stacks[dest] += src_crates
        self.stacks[src] = self.stacks[src][:-num]

    def top_crates(self) -> str:
        """List the top crates from each stack."""
        res = ""
        for _, val in sorted(self.stacks.items()):
            res += chr(val[-1])
        return res

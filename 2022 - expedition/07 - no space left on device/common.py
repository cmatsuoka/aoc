import fileinput
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(slots=True)
class _Directory:
    """Each directory node in the filesystem."""

    size: int = 0
    cumulative_size: int = 0
    parent: Optional["_Directory"] = None
    dirs: List["_Directory"] = field(default_factory=list)


class Filesystem:
    """The filesystem tree."""

    def __init__(self) -> None:
        self.sum_below_threshold = 0
        self._threshold = 0
        self._root: _Directory
        self._cwd: _Directory
        self._size = 0
        self._subdir_sizes: List[int] = []

    def parse(self, input_file: fileinput.FileInput) -> None:
        """Build the filesystem layout from the input commands."""
        for line in input_file:
            tokens = line.strip().split(" ")

            if tokens == ["$", "cd", "/"]:
                self._root = self._cwd = _Directory()
                self._cwd.parent = None
            elif tokens == ["$", "ls"]:
                self._size = 0
            elif tokens[0] == "dir":
                pass
            elif tokens[:2] == ["$", "cd"]:
                if self._size > 0:
                    self._cwd.size = self._size
                if tokens[2] == "..":
                    if not self._cwd.parent:
                        raise RuntimeError("root dir has no parent")
                    self._cwd = self._cwd.parent
                    self._size = 0
                else:
                    subdir = _Directory(parent=self._cwd)
                    self._cwd.dirs.append(subdir)
                    self._cwd = subdir
            else:
                self._size += int(tokens[0])

        self._cwd.size = self._size

    def add_sizes(self, *, threshold: int = 0) -> None:
        """Recursively determine cumulative directory sizes."""
        self.sum_below_threshold = 0
        self._threshold = threshold
        self._add_sizes(self._root)

    def _add_sizes(self, directory: _Directory) -> int:
        size = 0
        for child in directory.dirs:
            size += self._add_sizes(child)

        directory.cumulative_size = directory.size + size
        self._subdir_sizes.append(directory.cumulative_size)
        if directory.cumulative_size < self._threshold:
            self.sum_below_threshold += directory.cumulative_size

        return directory.cumulative_size

    def get_used_space(self) -> int:
        """Obtain the total space used in the filesystem."""
        return self._root.cumulative_size

    def dir_to_delete(self, *, space_to_free: int) -> int:
        """Obtain the size of the directory to delete."""
        for size in sorted(self._subdir_sizes):
            if size > space_to_free:
                return size

        raise RuntimeError("can't free space")

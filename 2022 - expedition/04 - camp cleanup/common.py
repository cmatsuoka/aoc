from dataclasses import dataclass


@dataclass(slots=True)
class SectionRange:
    """A range of sections defined by starting and ending section numbers."""

    start: int
    end: int

    @classmethod
    def parse(cls, range_str: str) -> "SectionRange":
        """Unmarshal start-end strings into a SectionRange class."""
        val1, val2 = range_str.split("-")
        start, end = int(val1), int(val2)
        assert start <= end
        return cls(start=start, end=end)

    def contains(self, other: "SectionRange") -> bool:
        """Whether this section range fully contains another section range."""
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other: "SectionRange") -> bool:
        """Whether this section range overlaps with another section range."""
        return self.start <= other.end and self.end >= other.start

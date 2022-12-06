from dataclasses import dataclass
from typing import Set


@dataclass
class Range:
    start: int
    end: int

    @classmethod
    def from_str(cls, range_string: str) -> "Range":
        start, end = range_string.split("-")
        return Range(start=int(start), end=int(end))

    def fully_contains(self, other: "Range") -> bool:
        return (self.start <= other.start) and (self.end >= other.end)

    def get_overlap(self, other: "Range") -> Set[int]:
        set_self = set(range(self.start, self.end + 1))
        set_other = set(range(other.start, other.end + 1))
        return set_self.intersection(set_other)


@dataclass
class RangePair:
    first: Range
    second: Range

    @classmethod
    def from_string(cls, pair_str: str) -> "RangePair":
        first_str, second_str = pair_str.split(",")
        return cls(first=Range.from_str(first_str), second=Range.from_str(second_str))

    def one_is_contained(self) -> bool:
        return self.first.fully_contains(self.second) or self.second.fully_contains(
            self.first
        )

    def do_overlap(self) -> bool:
        return len(self.first.get_overlap(self.second)) > 0

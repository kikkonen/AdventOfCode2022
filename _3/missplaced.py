from dataclasses import dataclass
from pathlib import Path
from typing import List, Set

from config import PRIORITY_BY_ITEM


@dataclass
class Bag:
    pocket1: Set[str]
    pocket2: Set[str]

    @property
    def common_item(self) -> str:
        common_item = list(self.pocket1.intersection(self.pocket2))
        if len(common_item) != 1:
            raise Exception(f"Expected exactly 1 missplaced item. Found {common_item}")
        return common_item[0]

    @classmethod
    def from_str(cls, contents: str) -> "Bag":
        if (size := len(contents)) % 2 != 0:
            raise Exception(f"Contents must be even, got {contents}")
        half = int(size / 2)
        return cls(pocket1=set(contents[:half]), pocket2=set(contents[half:]))


class MisplacedFinder:
    def __init__(self) -> None:
        self._bags = self._get_all_bags()

    def get_sum_of_prios_of_all_non_unique_items(self) -> int:
        non_unique_items = self._get_non_unique_items()
        return sum([PRIORITY_BY_ITEM[item] for item in non_unique_items])

    def _get_non_unique_items(self) -> List[str]:
        return [bag.common_item for bag in self._bags]

    def _get_all_bags(self) -> List[Bag]:
        path = Path(__file__).parent / "input.txt"
        bags = []
        with open(path, "r") as file:
            for line in file.read().splitlines():
                bags.append(Bag.from_str(line))
        return bags

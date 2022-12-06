from pathlib import Path
from typing import List

from definitions import RangePair


class OverlapFinder:
    def __init__(self) -> None:
        self._all_pairs: List[RangePair] = self._get_all_pairs()

    def get_number_of_pairs_that_fully_overlap(self):
        counter = 0
        for pair in self._all_pairs:
            if pair.one_is_contained():
                counter += 1
        return counter

    def get_number_pairs_that_overlap(self):
        counter = 0
        for pair in self._all_pairs:
            if pair.do_overlap():
                counter += 1
        return counter

    def _get_all_pairs(self) -> List[RangePair]:
        path = Path(__file__).parent / "input.txt"
        pairs = []
        with open(path, "r") as file:
            for line in file.read().splitlines():
                pairs.append(RangePair.from_string(line))
        return pairs

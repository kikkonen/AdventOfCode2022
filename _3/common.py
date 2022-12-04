from dataclasses import dataclass
from pathlib import Path
from typing import List, Set
from config import PRIORITY_BY_ITEM


@dataclass
class Group:

    bags: List[Set[str]]

    @property
    def common_item(self) -> str:
        common_items = self.bags[0]
        for bag in self.bags[1:]:
            common_items = common_items.intersection(bag)
        if len(common_items) != 1:
            raise Exception('Expected one a single item in common')
        return list(common_items)[0]

    @classmethod
    def from_list(cls, bags: List[str]) -> "Group":
        return Group(bags=[set(bag) for bag in bags])


class CommonItemFinder:

    def __init__(self, group_size: int) -> None:
        self._groups: List[Group] = self._load_all_groups(group_size)

    def get_sum_of_prios_of_common_items_per_group(self) -> int:
        common_items = [group.common_item for group in self._groups]
        return sum([PRIORITY_BY_ITEM[item] for item in common_items])
    
    def _load_all_groups(self, group_size: int) -> List[Group]:
        path = Path(__file__).parent / 'input.txt'
        with open(path, 'r') as file:
            lines = file.read().splitlines()
        if (n_lines := len(lines)) % group_size != 0:
            raise Exception(f'Number of lines must be multiple of group_size but found {n_lines=}')
        
        n_groups = int(n_lines / group_size)
        groups: List[Group] = []
        start = 0
        for group_number in range(n_groups):
            groups.append(Group.from_list(lines[start: start + group_size]))
            start += group_size
        return groups
        

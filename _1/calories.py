from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Elf:
    name: int
    calories: int


class CaloriesCounter:
    def __init__(self) -> None:
        self._lines = self._read_input()

    def get_top_n_elves_with_most_calories(self, top_n: int) -> List[Elf]:
        top_elves: List[Elf] = []

        calories_current = 0
        index_current = 0
        for calories in self._lines:
            if calories == "":
                if len(top_elves) == 0 or calories_current > top_elves[-1].calories:
                    current_elf = Elf(name=index_current, calories=calories_current)
                    top_elves = self._get_new_top_elves(top_elves, current_elf, top_n)
                calories_current = 0
                index_current += 1
            else:
                calories_current += int(calories)
        # if file doesnt end with a blank line then need to add last elf's count
        if len(top_elves) == 0 or calories_current > top_elves[-1].calories:
            final_elf = Elf(name=index_current, calories=calories_current)
            top_elves = self._get_new_top_elves(top_elves, final_elf, top_n)
        return top_elves

    @staticmethod
    def _read_input() -> List[str]:
        filepath = Path(__file__).parent / "input.txt"
        with open(filepath, "r") as file:
            return file.read().splitlines()

    @staticmethod
    def _get_new_top_elves(top_elves: List[Elf], new_elf: Elf, n_top: int) -> List[Elf]:
        combined_elves = top_elves + [new_elf]
        return sorted(combined_elves, key=lambda elf: elf.calories, reverse=True)[
            :n_top
        ]

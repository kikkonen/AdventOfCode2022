from functools import lru_cache
from pathlib import Path
from typing import List, Union

import numpy as np
from definitions import (
    INPUT_MAPPING,
    PAYOFF_CHOICE,
    PAYOFF_WIN_LOSE,
    RESULT_MAPPING,
    WIN_LOSE_MATRIX,
)


class MatchSimulatorBase:
    def __init__(self) -> None:
        self._moves = self._load_moves()

    @staticmethod
    def _load_moves() -> List[str]:
        path = Path(__file__).parent / "input.txt"
        with open(path, "r") as file:
            return file.read().splitlines()

    @lru_cache
    def _get_score(self, our_move: Union[str, int], opp_move: Union[str, int]) -> int:
        our_move_int = (
            INPUT_MAPPING[our_move] if isinstance(our_move, str) else our_move
        )
        opp_move_int = (
            INPUT_MAPPING[opp_move] if isinstance(opp_move, str) else opp_move
        )

        result = WIN_LOSE_MATRIX[our_move_int, opp_move_int]
        result_payoff = PAYOFF_WIN_LOSE[result]
        choice_payoff = PAYOFF_CHOICE[our_move_int]
        return result_payoff + choice_payoff


class MatchSimulatorPartOne(MatchSimulatorBase):
    def __init__(self) -> None:
        super().__init__()

    def simulate(self) -> int:
        score = 0
        for move in self._moves:
            opp_move, our_move = move.split(" ")
            round_score = self._get_score(our_move, opp_move)
            score += round_score
        return score


class MatchSimulatorPartTwo(MatchSimulatorBase):
    def __init__(self) -> None:
        super().__init__()

    def simulate(self) -> int:
        score = 0
        for move in self._moves:
            opp_move, round_result = move.split(" ")
            our_move = self._get_move_get_chosen_result(opp_move, round_result)
            round_score = self._get_score(our_move, opp_move)
            score += round_score
        return score

    @lru_cache
    def _get_move_get_chosen_result(
        self, opp_move: str, target_round_result: str
    ) -> int:
        target_result_int = RESULT_MAPPING[target_round_result]
        opp_move_int = INPUT_MAPPING[opp_move]
        return np.where(WIN_LOSE_MATRIX[:, opp_move_int] == target_result_int)[0][0]

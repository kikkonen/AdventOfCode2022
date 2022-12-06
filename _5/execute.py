from typing import Dict, List
from read import Instruction


class Executor:
    def __init__(self, stacks: Dict[int, List[str]]) -> None:
        self._stacks = stacks

    def execute_instruction(self, instruction: Instruction, preserve_order: bool):
        if not preserve_order:
            for _ in range(instruction.n_steps):
                self._stacks[instruction.to_stack].append(
                    self._stacks[instruction.from_stack].pop()
                )
        else:
            intermetiate_stack = []
            for _ in range(instruction.n_steps):
                intermetiate_stack.append(self._stacks[instruction.from_stack].pop())
            while len(intermetiate_stack) > 0:
                self._stacks[instruction.to_stack].append(intermetiate_stack.pop())

    def execute_all_instructions(self, instructions: List[Instruction], preserve_order: bool):
        for instruction in instructions:
            self.execute_instruction(instruction, preserve_order)

    def get_top_elements(self) -> List[str]:
        top_elements = []
        for i in range(1, len(self._stacks) + 1):
            top_elem = self._stacks[i][-1]
            top_elements.append(top_elem)
        return top_elements

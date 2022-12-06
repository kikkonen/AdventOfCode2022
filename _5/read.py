import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

pattern = re.compile(
    r"move (?P<n_steps>\d+) from (?P<from_stack>\d+) to (?P<to_stack>\d+)"
)


@dataclass
class Instruction:
    n_steps: int
    from_stack: int
    to_stack: int

    @classmethod
    def from_str(cls, instr_str: str):
        match = pattern.match(instr_str)
        if match is None:
            raise Exception(f"failed to match {instr_str}")
        match_dict = match.groupdict()
        return cls(
            n_steps=int(match_dict["n_steps"]),
            from_stack=int(match_dict["from_stack"]),
            to_stack=int(match_dict["to_stack"]),
        )


class InputReader:
    def read_all(self):
        stacks = defaultdict(list)
        instructions = []

        path = Path(__file__).parent / "input.txt"
        with open(path, "r") as file:
            lines = file.read().splitlines()
        for line in lines:
            if line.startswith("move"):
                instructions.append(Instruction.from_str(line))
            elif "[" in line:
                stack_number = 1
                pos_in_str = 1
                while pos_in_str < len(line):
                    value = line[pos_in_str]
                    if value != " ":
                        stacks[stack_number].append(value)
                    stack_number += 1
                    pos_in_str += 4
        stacks = {key: stack[::-1] for key, stack in stacks.items()}
        return stacks, instructions

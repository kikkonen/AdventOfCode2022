from execute import Executor
from read import InputReader

preserve_order = True

if __name__ == "__main__":
    stacks, instructions = InputReader().read_all()
    executor = Executor(stacks)
    executor.execute_all_instructions(instructions, preserve_order=preserve_order)
    print(f"{preserve_order=}", "".join(executor.get_top_elements()))

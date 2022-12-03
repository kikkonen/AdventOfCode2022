import numpy as np

# Notation: Rock, Paper and Scissors are mapped to 0, 1 and 2 respectively
# Defeat, Draw and Victory are mapped to -1, 0 and 1 respectively
# Context should be enough to tell whether 0/1 is referring to a choice of a result


# In the input, Rock is denoted by A or Y, Paper by B or X and Scissors by C or Z
INPUT_MAPPING = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}


# Indices represent your choice, columns your oponent choice
# E.g, (1, 0) is win (1) because you chose paper and opponent chose rock
WIN_LOSE_MATRIX = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])

# score based in the result
PAYOFF_WIN_LOSE = {-1: 0, 0: 3, 1: 6}

# Score based on the choice you've made
PAYOFF_CHOICE = {0: 1, 1: 2, 2: 3}

# Result mapping for second part
RESULT_MAPPING = {"X": -1, "Y": 0, "Z": 1}

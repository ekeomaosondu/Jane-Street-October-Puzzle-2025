import torch
from matplotlib import pyplot as plt

def q_of_p(p):
    # Stores the subgame payoff matrices
    dp_payoff_matrices = [] 

    #Stores the expected value of each subgame
    dp_expected_values = [] 

    # Stores the frequency with which the batter swings
    # (equal to probability that pitcher throws strike by symmetry)
    dp_swing_strike_frequencies = [] 

    # Initialize with starting values
    for i in range(3):
        dp_payoff_matrices.append([])
        dp_swing_strike_frequencies.append([])
        dp_expected_values.append([])
        for j in range(4):
            dp_payoff_matrices[-1].append([0, 0, 0, 0])
            dp_swing_strike_frequencies[-1].append(0)
            dp_expected_values[-1].append(0)
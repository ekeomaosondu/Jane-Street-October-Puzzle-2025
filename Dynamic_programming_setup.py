import torch
from matplotlib import pyplot as plt

def q_of_p(p): #The probaility of reaching full count P(Homerun) = p

    #Full Count Parameters
    STRIKES = 2
    BALLS = 3



    # Stores the subgame payoff matrices
    # The payoff matrices in this implementation are of the following form:

    #           Strike            Ball
    # 
    #  Swing    EV of Swing     EV of Strike
    #
    #   Wait    EV of Strike     EV of Ball
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

    # Subroutine to compute the strategy and expected value of a payoff matrix
    # Expects 2 x 2 payoff matrix of the form matrix = flatten([[a, b], [c, d]])
    def compute_ev(payoffs):
        a, b, c, d = payoffs
        prob = (d - b) / (a + d - b - c)

        # return tuple of the batter's expected value and the swing probability.
        return a * prob + (1 - prob) * b, prob
    
    # Build DP table in reverse topological order
    for strikes in range(STRIKES, -1, -1):
        for balls in range(BALLS, -1, -1):

            # If state corresponds to 3 balls
            if balls == BALLS:
                # Expected value of ball is 1
                expected_value_ball = 1
            else:
                # Otherwise, we take the expected value of the next reached subgame
                expected_value_ball = dp_expected_values[strikes][balls + 1]

            dp_payoff_matrices[strikes][balls][3] += expected_value_ball
            

            #The EV of a swing is 4 * P(Home Run) + EV of Strike * (1 - P(Home Run))
            dp_payoff_matrices[strikes][balls][0] += 4 * p
            

            if strikes != STRIKES:
                dp_payoff_matrices[strikes][balls][0] += dp_expected_values[strikes + 1][balls] * (1-p)
                dp_payoff_matrices[strikes][balls][1] += dp_expected_values[strikes + 1][balls]
                dp_payoff_matrices[strikes][balls][2] += dp_expected_values[strikes + 1][balls]

            dp_expected_values[strikes][balls], dp_swing_strike_frequencies[strikes][balls] = compute_ev(dp_payoff_matrices[strikes][balls])

    #Initialize Full Count State Reach Probabilities
    dp_q = []
    for i in range(STRIKES + 1):
        dp_q.append([])
        for j in range(BALLS + 1):
            dp_q[-1].append(0)

    
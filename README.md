Solving Jane Street's October 2025 Puzzle involved Game Theory, Markov Probability Theory, Dynamic Programming & Optimization

In my solution, we first solve for the payoff matrices for each individual subgame where the batter has (b balls, s strikes).

These payoffs are defined in terms of the expected values of other subgames. 
  First, set up a reverse topological order of the subgames. 
  In this order solve for the indivividual payoff matrices.
  For instance:
    If the state has 3 balls, the payoff of another ball is 1.
    If the state has 2 strikes, the payoff of another strike is 0.
    Otherwise, the payoff of a strike is the ev of the state with b balls and s + 1 strikes (and similar for balls).
    The payoff of homerun is parametric in p.

Due to structure of the subgames, both players will play a mixed strategy. We solve for the optimal mixing frequency using the law of indifference (Parametric in p).

With the frequencies, we can compute the probability of reaching the state (b = 3, s = 2) with another dynamic programming (Fill the table values in reverse topo order) (Parametric in p)

Finally we have a function that given p, computes the probability q of reaching full count.

We optimize this function q(p) using Adam Optimizer.


Below is q plotted against p for many values:
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/36bcb8ce-b0d8-4844-a129-7586fafd0716" />

# Experiment 7: Associative Memory with Graph Plotting
# This plots stored and recalled bipolar patterns.
import numpy as np
import matplotlib.pyplot as plt

# Store one pattern
pattern = np.array([1, -1, 1, 1])
weights = np.outer(pattern, pattern)
np.fill_diagonal(weights, 0)

# Recall from a noisy pattern
test = np.array([1, 1, 1, -1])
net = weights @ test
recalled = np.where(net >= 0, 1, -1)

# Plot patterns as simple line graphs
positions = [1, 2, 3, 4]
plt.plot(positions, pattern, marker='o', label='Stored pattern')
plt.plot(positions, test, marker='s', label='Noisy input')
plt.plot(positions, recalled, marker='^', label='Recalled pattern')
plt.xlabel("Pattern position")
plt.ylabel("Value")
plt.title("Associative Memory Pattern Recall")
plt.xticks(positions)
plt.yticks([-1, 1])
plt.grid(True)
plt.legend()
plt.show()

# Theory: Associative memory recalls a stored pattern from a partial or noisy
# version. The graph compares stored, noisy and recalled values.

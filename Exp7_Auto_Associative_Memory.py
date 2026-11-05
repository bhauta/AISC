# Experiment 7: Auto-associative Memory
import numpy as np

# Store a pattern in the weight matrix
pattern = np.array([[-1, 1, 1, 1]])
weights = pattern.T @ pattern
print("Weight matrix:")
print(weights)

# Recall a noisy version of the stored pattern
test = np.array([[-1, -1, 1, 1]])
net = test @ weights
output = np.where(net > 0, 1, -1)
print("Net input:", net)
print("Recalled pattern:", output)

# Theory: Auto-associative memory stores and recalls the same pattern.
# A noisy input is corrected using the learned weight matrix.

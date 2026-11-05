# Experiment 7: Bidirectional Associative Memory (BAM)
import numpy as np

# Training input and target pairs
X = np.array([[1,-1,1], [-1,1,-1]])
T = np.array([[-1,1], [1,-1]])

# Create weight matrix
weights = X.T @ T
print("Weight matrix:")
print(weights)

# Recall in forward direction
test = np.array([[1,-1,1]])
net = test @ weights
target = np.where(net > 0, 1, -1)
print("Forward output:", target)

# Recall in reverse direction
net_reverse = target @ weights.T
input_pattern = np.where(net_reverse > 0, 1, -1)
print("Reverse output:", input_pattern)

# Theory: BAM stores paired patterns and recalls from input to target
# and from target back to input.

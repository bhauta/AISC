# Experiment 7: Hetero-associative Memory
import numpy as np

# Input patterns and their associated target patterns
X = np.array([[1,0,0,0], [1,1,0,0], [0,0,0,1], [0,0,1,1]])
T = np.array([[0,1], [0,1], [1,0], [1,0]])

# Create the weight matrix
weights = X.T @ T
print("Weight matrix:")
print(weights)

# Recall target for a test input
test = np.array([[1,1,0,0]])
net = test @ weights
output = np.where(net > 0, 1, 0)
print("Net input:", net)
print("Output:", output)

# Theory: Hetero-associative memory stores a relationship between input
# patterns and different target patterns.

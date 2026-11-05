# Experiment 5: Backpropagation using one training example
import math

# Input, target, learning rate
x1 = 0.5
x2 = 0.6
target = 1
lr = 0.1

# Input-to-hidden weights and biases
v11, v21, v01 = 0.2, 0.3, 0.1
v12, v22, v02 = 0.4, 0.5, 0.1

# Hidden-to-output weights and bias
w1, w2, w0 = 0.3, 0.4, 0.1

def sigmoid(value):
    return 1 / (1 + math.exp(-value))

# Train for four epochs
for epoch in range(4):
    z1 = sigmoid(x1*v11 + x2*v21 + v01)
    z2 = sigmoid(x1*v12 + x2*v22 + v02)
    output = sigmoid(z1*w1 + z2*w2 + w0)
    error = target - output

    # Calculate output and hidden layer deltas
    delta = output*(1-output)*error
    delta_z1 = z1*(1-z1)*delta*w1
    delta_z2 = z2*(1-z2)*delta*w2

    # Update output layer parameters
    w1 += lr*delta*z1
    w2 += lr*delta*z2
    w0 += lr*delta

    # Update hidden layer parameters
    v11 += lr*delta_z1*x1
    v21 += lr*delta_z1*x2
    v01 += lr*delta_z1
    v12 += lr*delta_z2*x1
    v22 += lr*delta_z2*x2
    v02 += lr*delta_z2

    print("Epoch:", epoch+1, "Output:", round(output,4), "Error:", round(error,4))

# Theory: Backpropagation computes output error and propagates it backward
# to adjust network weights using gradient-based learning.

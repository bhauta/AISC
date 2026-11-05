# Experiment 4: Perceptron Learning

# Training data for the AND-like bipolar function
inputs = [[1,1], [1,-1], [-1,1], [-1,-1]]
targets = [1,-1,-1,-1]

# Initial parameters
w1 = 0
w2 = 0
bias = 0
learning_rate = 1

# Train the perceptron
for epoch in range(20):
    errors = 0
    for i in range(len(inputs)):
        net = w1*inputs[i][0] + w2*inputs[i][1] + bias

        if net > 0:
            output = 1
        elif net < 0:
            output = -1
        else:
            output = 0

        if output != targets[i]:
            w1 = w1 + learning_rate*targets[i]*inputs[i][0]
            w2 = w2 + learning_rate*targets[i]*inputs[i][1]
            bias = bias + learning_rate*targets[i]
            errors += 1

    print("Epoch", epoch+1, "Weights:", w1, w2, "Bias:", bias)
    if errors == 0:
        break

# Theory: A perceptron is a simple neuron that learns a linear decision boundary
# by updating its weights and bias whenever it makes a classification error.

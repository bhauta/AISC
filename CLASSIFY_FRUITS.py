# Perceptron classification: Apple (1) or Orange (0)
# Features: shape(round=1), texture(smooth=1), weight(heavy=1)

def predict(features, weights, bias):
    total = bias
    for i in range(len(features)):
        total += features[i] * weights[i]
    if total >= 0:
        return 1
    return 0

# Small labeled training set: [shape, texture, weight]
training_data = [
    ([1, 1, 1], 1), ([1, 1, 0], 1), ([0, 0, 1], 0),
    ([0, 0, 0], 0), ([1, 0, 1], 1), ([0, 1, 0], 0)
]
weights = [0.0, 0.0, 0.0]
bias = 0.0
learning_rate = 0.1

# Supervised perceptron training
for epoch in range(20):
    for features, target in training_data:
        output = predict(features, weights, bias)
        error = target - output
        for i in range(3):
            weights[i] += learning_rate * error * features[i]
        bias += learning_rate * error

# Test unseen fruit samples
new_fruits = [
    ([1, 1, 1], "Fruit 1"),
    ([0, 0, 1], "Fruit 2"),
    ([1, 0, 0], "Fruit 3")
]
for features, name in new_fruits:
    result = predict(features, weights, bias)
    if result == 1:
        label = "Apple"
    else:
        label = "Orange"
    print(name, features, "->", label)

# Theory: A perceptron learns a binary decision boundary from labeled examples
# by updating weights and bias when its prediction is incorrect.

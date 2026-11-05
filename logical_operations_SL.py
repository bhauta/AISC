# Single-layer perceptron for AND, OR and NOT gates

# Perceptron step function
def perceptron(inputs, weights, bias):
    total = bias
    for i in range(len(inputs)):
        total += inputs[i] * weights[i]
    if total >= 0:
        return 1
    return 0

# AND and OR gates
and_weights = [1, 1]
and_bias = -1.5
or_weights = [1, 1]
or_bias = -0.5

print("A B | AND OR")
for a in [0, 1]:
    for b in [0, 1]:
        print(a, b, "|", perceptron([a, b], and_weights, and_bias),
              perceptron([a, b], or_weights, or_bias))

# NOT gate
print("\nA | NOT")
for a in [0, 1]:
    print(a, "|", perceptron([a], [-1], 0.5))

# Theory: A single-layer perceptron computes a weighted sum and applies a
# threshold. AND, OR and NOT are linearly separable and can be learned.

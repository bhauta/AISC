# XOR using a small perceptron network (two-layer arrangement)

def step(value):
    if value >= 0:
        return 1
    return 0

def perceptron(inputs, weights, bias):
    total = bias
    for i in range(len(inputs)):
        total += inputs[i] * weights[i]
    return step(total)

# Hidden neurons form (A AND NOT B) and (NOT A AND B)
def xor(a, b):
    h1 = perceptron([a, b], [1, -1], -0.5)
    h2 = perceptron([a, b], [-1, 1], -0.5)
    return perceptron([h1, h2], [1, 1], -0.5)

print("A B | XOR")
for a in [0, 1]:
    for b in [0, 1]:
        print(a, b, "|", xor(a, b))

# Theory: XOR is not linearly separable, so one perceptron cannot learn it.
# A hidden layer combines two linearly separable patterns to produce XOR.

# Hopfield network for storing and recalling small handwritten digit patterns
# Uses sklearn's built-in 8x8 digits dataset (MNIST-like) to avoid large downloads.
# For full 28x28 MNIST, replace the data-loading section with keras MNIST.
import random

try:
    from sklearn.datasets import load_digits
except ImportError:
    print("Install scikit-learn: pip install scikit-learn")
    raise

# Select two digit images and convert pixels to bipolar values (-1, +1)
dataset = load_digits()
patterns = []
for wanted_digit in [0, 1]:
    for i in range(len(dataset.target)):
        if dataset.target[i] == wanted_digit:
            image = dataset.images[i]
            pattern = []
            for row in image:
                for pixel in row:
                    if pixel >= 8:
                        pattern.append(1)
                    else:
                        pattern.append(-1)
            patterns.append(pattern)
            break

# Hebbian learning: add outer products and clear self-connections
size = len(patterns[0])
weights = [[0.0 for j in range(size)] for i in range(size)]
for pattern in patterns:
    for i in range(size):
        for j in range(size):
            if i != j:
                weights[i][j] += pattern[i] * pattern[j]

# Corrupt the first pattern by flipping a few pixels
original = patterns[0][:]
noisy = original[:]
random.seed(7)
for i in range(8):
    position = random.randrange(size)
    noisy[position] *= -1

# Recall using asynchronous updates until stable or iteration limit
recalled = noisy[:]
for iteration in range(20):
    changed = False
    for i in range(size):
        total = 0
        for j in range(size):
            total += weights[i][j] * recalled[j]
        new_value = 1 if total >= 0 else -1
        if new_value != recalled[i]:
            recalled[i] = new_value
            changed = True
    if not changed:
        break

# Compare recall with stored pattern
matches = 0
for i in range(size):
    if recalled[i] == original[i]:
        matches += 1
print("Recall pixel accuracy:", round(matches / size * 100, 2), "%")

def show_pattern(pattern):
    for row in range(8):
        line = ""
        for col in range(8):
            if pattern[row * 8 + col] == 1:
                line += "##"
            else:
                line += "  "
        print(line)

print("Original digit pattern:")
show_pattern(original)
print("Recalled pattern:")
show_pattern(recalled)

# Theory: A Hopfield network stores patterns in symmetric weights using Hebbian
# learning. Repeated neuron updates move a noisy input toward a stored pattern.

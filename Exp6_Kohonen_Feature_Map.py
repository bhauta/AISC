# Experiment 6: Kohonen Feature Map (SOM)
X = [0.2, 0.4]
learning_rate = 0.2
weights = [[0.3,0.5], [0.2,0.6], [0.1,0.7], [0.8,0.9], [0.4,0.2]]

# Find the closest weight vector
distances = []
for weight in weights:
    distance = 0
    for i in range(len(X)):
        distance += (X[i]-weight[i])**2
    distances.append(distance)

winner = distances.index(min(distances))

# Move the winner toward the input
for i in range(len(X)):
    weights[winner][i] += learning_rate*(X[i]-weights[winner][i])

print("Winner:", winner)
print("Updated weights:", weights)

# Theory: A Self-Organizing Map selects the closest neuron and adjusts its
# weight vector toward the input, preserving similarity in the map.

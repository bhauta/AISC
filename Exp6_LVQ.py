# Experiment 6: Learning Vector Quantization (LVQ)
X = [[0,0,1,1], [1,0,0,0], [0,0,0,1], [1,1,0,0], [0,1,1,0]]
targets = [1,2,2,1,1]
weights = [[0,0,1,1], [1,0,0,0]]
weight_classes = [1,2]
learning_rate = 0.1

# Train using the remaining input patterns
for k in range(2, len(X)):
    x = X[k]
    distances = []

    for weight in weights:
        distance = 0
        for i in range(len(x)):
            distance += (x[i]-weight[i])**2
        distances.append(distance)

    winner = distances.index(min(distances))
    print("Input:", x, "Target:", targets[k], "Winner:", winner+1)

    # Move winner toward correct class, away from wrong class
    if weight_classes[winner] == targets[k]:
        for i in range(len(x)):
            weights[winner][i] += learning_rate*(x[i]-weights[winner][i])
    else:
        for i in range(len(x)):
            weights[winner][i] -= learning_rate*(x[i]-weights[winner][i])

    print("Updated winner:", weights[winner])

print("Final weights:", weights)

# Theory: LVQ is a supervised classification method. The closest prototype
# moves toward an input when its class is correct and away otherwise.

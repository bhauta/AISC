# Binary neural network for customer churn prediction
# CSV format (save as telco_dummy.csv):
# tenure,monthly_charges,total_charges,support_calls,churn
# 2,80,160,4,1
# 24,60,1440,1,0
# 5,95,475,3,1
# 36,55,1980,0,0
# 12,75,900,2,0
# 3,100,300,5,1
# This file uses small dummy data below so it runs without an external dataset.
# Replace the list with rows loaded from your own CSV when available.

import math

# Features are scaled to roughly 0..1; target: churn=1, retained=0
rows = [
    ([2/72, 80/120, 160/2500, 4/6], 1),
    ([24/72, 60/120, 1440/2500, 1/6], 0),
    ([5/72, 95/120, 475/2500, 3/6], 1),
    ([36/72, 55/120, 1980/2500, 0/6], 0),
    ([12/72, 75/120, 900/2500, 2/6], 0),
    ([3/72, 100/120, 300/2500, 5/6], 1),
    ([48/72, 65/120, 2400/2500, 1/6], 0),
    ([8/72, 90/120, 720/2500, 4/6], 1)
]

def sigmoid(value):
    return 1 / (1 + math.exp(-value))

# Initialize a small neural network: 4 inputs, 3 hidden neurons, 1 output
w1 = [[0.1, -0.2, 0.3], [0.2, 0.1, -0.1],
      [-0.1, 0.2, 0.1], [0.3, -0.1, 0.2]]
b1 = [0.0, 0.0, 0.0]
w2 = [0.2, -0.3, 0.1]
b2 = 0.0
lr = 0.5

# Train using binary cross-entropy gradient for sigmoid output
for epoch in range(1500):
    for features, target in rows:
        hidden = []
        for j in range(3):
            total = b1[j]
            for i in range(4):
                total += features[i] * w1[i][j]
            hidden.append(sigmoid(total))
        output_sum = b2
        for j in range(3):
            output_sum += hidden[j] * w2[j]
        output = sigmoid(output_sum)
        delta_out = target - output
        delta_hidden = []
        for j in range(3):
            delta_hidden.append(hidden[j] * (1-hidden[j]) * delta_out * w2[j])
        for j in range(3):
            w2[j] += lr * delta_out * hidden[j]
        b2 += lr * delta_out
        for i in range(4):
            for j in range(3):
                w1[i][j] += lr * delta_hidden[j] * features[i]
        for j in range(3):
            b1[j] += lr * delta_hidden[j]

# Evaluate predictions on the dummy examples
correct = 0
print("Actual | Predicted churn")
for features, target in rows:
    hidden = []
    for j in range(3):
        total = b1[j]
        for i in range(4):
            total += features[i] * w1[i][j]
        hidden.append(sigmoid(total))
    total = b2
    for j in range(3):
        total += hidden[j] * w2[j]
    probability = sigmoid(total)
    prediction = 1 if probability >= 0.5 else 0
    print(target, "|", prediction, "probability:", round(probability, 3))
    if prediction == target:
        correct += 1
print("Dummy-data accuracy:", round(correct / len(rows) * 100, 2), "%")

# Theory: A sigmoid neural network learns churn probability from customer
# features. The sigmoid output is thresholded for binary classification.
# Real projects should use train/test splits, SMOTE if needed, ROC-AUC and
# precision-recall metrics; this tiny dummy dataset is for lab demonstration.

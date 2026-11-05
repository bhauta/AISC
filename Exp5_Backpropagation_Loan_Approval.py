# Experiment 5: Backpropagation for Loan Approval
# CSV format: Income,Age,CreditScore,Approved (header row included)
import csv
import math

filename = input("Enter CSV filename: ")
X = []
targets = []

# Read and normalize the data
with open(filename, "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        X.append([int(row[0])/120000, int(row[1])/60, int(row[2])/850])
        targets.append(int(row[3]))

# Initial network weights
W1 = [[0.2,0.3,0.4], [0.1,0.5,0.2], [0.3,0.2,0.1]]
W2 = [0.3,0.4,0.2]
b1 = [0.1,0.1,0.1]
b2 = 0.1
lr = 0.5

def sigmoid(value):
    return 1/(1+math.exp(-value))

# Train the network
for epoch in range(500):
    for n in range(len(X)):
        hidden = []
        for j in range(3):
            total = b1[j]
            for k in range(3):
                total += X[n][k]*W1[k][j]
            hidden.append(sigmoid(total))

        output = sigmoid(hidden[0]*W2[0] + hidden[1]*W2[1] + hidden[2]*W2[2] + b2)
        error = targets[n] - output
        delta_out = error*output*(1-output)

        delta_hidden = []
        for j in range(3):
            delta_hidden.append(hidden[j]*(1-hidden[j])*delta_out*W2[j])

        for j in range(3):
            W2[j] += lr*delta_out*hidden[j]
        b2 += lr*delta_out

        for j in range(3):
            for k in range(3):
                W1[k][j] += lr*delta_hidden[j]*X[n][k]
            b1[j] += lr*delta_hidden[j]

# Predict training samples
print("Predictions:")
for row in X:
    hidden = []
    for j in range(3):
        total = b1[j]
        for k in range(3):
            total += row[k]*W1[k][j]
        hidden.append(sigmoid(total))
    output = sigmoid(hidden[0]*W2[0] + hidden[1]*W2[1] + hidden[2]*W2[2] + b2)
    if output >= 0.5:
        print("Approved")
    else:
        print("Not Approved")

# Predict a new applicant
income = int(input("Income: "))
age = int(input("Age: "))
credit = int(input("Credit score: "))
new = [income/120000, age/60, credit/850]
hidden = []
for j in range(3):
    total = b1[j]
    for k in range(3):
        total += new[k]*W1[k][j]
    hidden.append(sigmoid(total))
prediction = sigmoid(hidden[0]*W2[0] + hidden[1]*W2[1] + hidden[2]*W2[2] + b2)
print("Prediction:", round(prediction,4))
if prediction >= 0.5:
    print("Loan Approved")
else:
    print("Loan Not Approved")

# Theory: Backpropagation trains a neural network from labeled examples.
# Income, age and credit score are inputs; the output predicts loan approval.

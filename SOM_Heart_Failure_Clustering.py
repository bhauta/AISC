# Kohonen Self-Organizing Map for simple patient risk clustering
# Dummy clinical features are used; this is an educational example, not diagnosis.
import math

# [age, ejection_fraction, serum_creatinine, blood_pressure, diabetes]
# Scale each feature to approximately 0..1
patients = [
    [0.80, 0.25, 0.80, 0.55, 1],
    [0.70, 0.30, 0.70, 0.60, 1],
    [0.45, 0.55, 0.35, 0.70, 0],
    [0.50, 0.60, 0.30, 0.75, 0],
    [0.85, 0.20, 0.90, 0.45, 1],
    [0.40, 0.70, 0.25, 0.80, 0]
]

# Initialize three SOM neurons (prototype vectors)
weights = [
    [0.3, 0.7, 0.3, 0.7, 0.0],
    [0.6, 0.5, 0.5, 0.6, 0.5],
    [0.8, 0.3, 0.8, 0.5, 1.0]
]
learning_rate = 0.4

# Train: find the closest neuron and move its weights toward the patient
for epoch in range(100):
    for patient in patients:
        distances = []
        for neuron in weights:
            distance = 0
            for i in range(len(patient)):
                distance += (patient[i] - neuron[i]) ** 2
            distances.append(math.sqrt(distance))
        winner = distances.index(min(distances))
        for i in range(len(patient)):
            weights[winner][i] += learning_rate * (patient[i] - weights[winner][i])
    learning_rate *= 0.98

# Assign patients to clusters and show simple risk profiles
clusters = [[], [], []]
for index, patient in enumerate(patients):
    distances = []
    for neuron in weights:
        distance = 0
        for i in range(len(patient)):
            distance += (patient[i] - neuron[i]) ** 2
        distances.append(distance)
    winner = distances.index(min(distances))
    clusters[winner].append(index + 1)

print("Patient clusters (patient numbers):")
for i in range(3):
    print("Cluster", i + 1, ":", clusters[i])
    print("Prototype:", [round(value, 2) for value in weights[i]])

# Theory: SOM is an unsupervised competitive-learning method. Similar patient
# feature vectors map to the same prototype. Cluster profiles can suggest
# relative risk patterns, but must not be used as clinical decisions.

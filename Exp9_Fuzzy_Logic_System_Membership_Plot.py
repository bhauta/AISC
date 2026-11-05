# Experiment 9: Fuzzy Logic System Design - Membership Function Plot
import numpy as np
import matplotlib.pyplot as plt

# Simple triangular membership function
def triangular(x, a, b, c):
    # Handle left- and right-shoulder triangles
    if a == b and x == a:
        return 1
    if b == c and x == c:
        return 1
    if x < a or x > c:
        return 0
    if x == b:
        return 1
    if x < b:
        return (x-a)/(b-a)
    return (c-x)/(c-b)

# Temperature range and fuzzy sets
temperature = np.arange(0, 41, 1)
cold = []
warm = []
hot = []

for value in temperature:
    cold.append(triangular(value, 0, 0, 20) if value < 20 else 0)
    warm.append(triangular(value, 10, 25, 40))
    hot.append(triangular(value, 30, 40, 40) if value > 30 else 0)

# Plot membership functions
plt.plot(temperature, cold, label='Cold')
plt.plot(temperature, warm, label='Warm')
plt.plot(temperature, hot, label='Hot')
plt.xlabel('Temperature')
plt.ylabel('Membership degree')
plt.title('Temperature Membership Functions')
plt.grid(True)
plt.legend()
plt.show()

# Theory: Membership functions map crisp values to degrees between 0 and 1.
# These sets describe temperature as cold, warm or hot.

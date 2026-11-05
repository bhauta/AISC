# Fuzzy controller for green-light duration using traffic density and wait time
# Inputs: density (0-100), waiting time (0-120 seconds); output: green time

def triangle(x, a, b, c):
    if x <= a or x >= c:
        if x == b:
            return 1.0
        return 0.0
    if x == b:
        return 1.0
    if x < b:
        return (x - a) / (b - a)
    return (c - x) / (c - b)

def memberships(value, sets):
    result = []
    for a, b, c in sets:
        result.append(triangle(value, a, b, c))
    return result

# Low, medium and high fuzzy sets
density_sets = [(0, 0, 50), (20, 50, 80), (50, 100, 100)]
wait_sets = [(0, 0, 60), (20, 60, 100), (60, 120, 120)]

# Rule output values in seconds: short=20, medium=40, long=60
rule_outputs = [20, 40, 60]

def controller(density, waiting):
    d = memberships(density, density_sets)
    w = memberships(waiting, wait_sets)
    strengths = [0.0, 0.0, 0.0]

    # Rule table: rows density low/medium/high, columns wait low/medium/high
    rules = [
        [0, 0, 1],
        [0, 1, 2],
        [1, 2, 2]
    ]
    for i in range(3):
        for j in range(3):
            strength = min(d[i], w[j])
            output_index = rules[i][j]
            if strength > strengths[output_index]:
                strengths[output_index] = strength

    # Simple weighted average defuzzification
    numerator = 0.0
    denominator = 0.0
    for i in range(3):
        numerator += strengths[i] * rule_outputs[i]
        denominator += strengths[i]
    if denominator == 0:
        return 20
    return numerator / denominator

# Example intersection input
traffic_density = 75
waiting_time = 80
green_duration = controller(traffic_density, waiting_time)
print("Traffic density:", traffic_density)
print("Waiting time:", waiting_time, "seconds")
print("Green light duration:", round(green_duration, 2), "seconds")

# Theory: Fuzzy control converts traffic inputs into memberships, applies
# IF-THEN rules, and combines rule outputs to choose a green-light duration.

# Fuzzy relationship between AQI levels and possible health effects
# Membership values are illustrative and are not medical advice.

# Membership functions for AQI categories: Good, Moderate, Poor, Severe

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

def left_shoulder(x, a, b):
    if x <= a:
        return 1.0
    if x >= b:
        return 0.0
    return (b - x) / (b - a)

def right_shoulder(x, a, b):
    if x <= a:
        return 0.0
    if x >= b:
        return 1.0
    return (x - a) / (b - a)

def aqi_membership(aqi):
    good = left_shoulder(aqi, 0, 50)
    moderate = triangle(aqi, 30, 100, 150)
    poor = triangle(aqi, 100, 200, 300)
    severe = right_shoulder(aqi, 250, 400)
    return [good, moderate, poor, severe]

# Relation from air-quality categories to health-effect categories
# Rows: Good, Moderate, Poor, Severe; columns: Healthy, Mild, Serious
R = [
    [1.0, 0.0, 0.0],
    [0.7, 0.3, 0.0],
    [0.2, 0.7, 0.4],
    [0.0, 0.3, 1.0]
]

# Fuzzy composition: AQI category membership composed with health relation
def health_effects(aqi):
    memberships = aqi_membership(aqi)
    effects = []
    for j in range(3):
        values = []
        for i in range(4):
            values.append(min(memberships[i], R[i][j]))
        effects.append(max(values))
    return memberships, effects

# Demonstrate the three requested AQI values
labels_a = ["Good", "Moderate", "Poor", "Severe"]
labels_h = ["Healthy", "Mild Symptoms", "Serious Symptoms"]
for aqi in [40, 120, 250]:
    memberships, effects = health_effects(aqi)
    print("\nAQI:", aqi)
    for i in range(4):
        print(labels_a[i], ":", round(memberships[i], 2))
    for i in range(3):
        print(labels_h[i], ":", round(effects[i], 2))

# Theory: Fuzzy sets represent overlapping AQI categories. Max-min composition
# maps AQI membership through a fuzzy relation to possible health effects.

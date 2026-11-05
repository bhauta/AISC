# Experiment 9: Temperature and Humidity Fan Controller
# Requires: pip install scikit-fuzzy numpy
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define input and output variables
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Define membership functions
temperature['cold'] = fuzz.trimf(temperature.universe, [0,0,20])
temperature['warm'] = fuzz.trimf(temperature.universe, [10,25,40])
temperature['hot'] = fuzz.trimf(temperature.universe, [30,40,40])

humidity['low'] = fuzz.trimf(humidity.universe, [0,0,50])
humidity['medium'] = fuzz.trimf(humidity.universe, [30,50,70])
humidity['high'] = fuzz.trimf(humidity.universe, [50,100,100])

fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0,0,50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [30,50,70])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50,100,100])

# Define fuzzy rules
rules = [
    ctrl.Rule(temperature['cold'] & humidity['low'], fan_speed['low']),
    ctrl.Rule(temperature['cold'] & humidity['medium'], fan_speed['low']),
    ctrl.Rule(temperature['cold'] & humidity['high'], fan_speed['medium']),
    ctrl.Rule(temperature['warm'] & humidity['low'], fan_speed['low']),
    ctrl.Rule(temperature['warm'] & humidity['medium'], fan_speed['medium']),
    ctrl.Rule(temperature['warm'] & humidity['high'], fan_speed['high']),
    ctrl.Rule(temperature['hot'] & humidity['low'], fan_speed['medium']),
    ctrl.Rule(temperature['hot'] & humidity['medium'], fan_speed['high']),
    ctrl.Rule(temperature['hot'] & humidity['high'], fan_speed['high'])
]

# Run the controller
system = ctrl.ControlSystem(rules)
simulation = ctrl.ControlSystemSimulation(system)
simulation.input['temperature'] = 25
simulation.input['humidity'] = 60
simulation.compute()
print("Fan speed:", simulation.output['fan_speed'])

# Theory: A fuzzy controller converts crisp inputs into fuzzy memberships,
# applies IF-THEN rules, and produces a crisp output using defuzzification.

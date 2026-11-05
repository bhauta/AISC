# Experiment 3: Logic Gates and Adders

# Basic threshold neuron
def neuron(a, b, threshold):
    total = a + b
    if total >= threshold:
        return 1
    return 0

def and_gate(a, b):
    return neuron(a, b, 2)

def or_gate(a, b):
    return neuron(a, b, 1)

def not_gate(a):
    return 1 - a

def nand_gate(a, b):
    return 1 - and_gate(a, b)

def xor_gate(a, b):
    first = and_gate(a, not_gate(b))
    second = and_gate(not_gate(a), b)
    return or_gate(first, second)

# Print truth tables
print("A B | AND OR NAND XOR")
for a, b in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    print(a, b, "|", and_gate(a,b), or_gate(a,b), nand_gate(a,b), xor_gate(a,b))

# Half adder
print("\\nHalf Adder: A B | SUM CARRY")
for a, b in [(0,0), (0,1), (1,0), (1,1)]:
    sum_out = xor_gate(a,b)
    carry = and_gate(a,b)
    print(a,b,"|",sum_out,carry)

# Full adder
print("\\nFull Adder: A B Cin | SUM CARRY")
for a,b,cin in [(0,0,0),(0,0,1),(0,1,0),(0,1,1),
                 (1,0,0),(1,0,1),(1,1,0),(1,1,1)]:
    sum_out = xor_gate(xor_gate(a,b),cin)
    carry = or_gate(and_gate(a,b), and_gate(cin,xor_gate(a,b)))
    print(a,b,cin,"|",sum_out,carry)

# Theory: Logic gates perform Boolean operations. A half adder adds two bits;
# a full adder adds two bits and a carry input.

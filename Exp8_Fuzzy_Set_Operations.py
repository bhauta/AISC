# Experiment 8: Fuzzy Set Operations

# Membership values of two fuzzy sets
elements = [0.64, 0.645, 0.65, 0.655, 0.66]
A = [0, 0.75, 1, 0.5, 0]
B = [0, 0.25, 0.75, 1, 0.5]

union = []
intersection = []
complement_A = []
complement_B = []

# Standard fuzzy operations
for i in range(len(A)):
    union.append(max(A[i], B[i]))
    intersection.append(min(A[i], B[i]))
    complement_A.append(1-A[i])
    complement_B.append(1-B[i])

print("Union:", union)
print("Intersection:", intersection)
print("Complement A:", complement_A)
print("Complement B:", complement_B)

# Algebraic and bounded operations
A = [0.2, 0.3, 0.4, 0.5]
B = [0.1, 0.2, 0.2, 1.0]
algebraic_sum = []
algebraic_product = []
bounded_sum = []
bounded_difference = []

for i in range(len(A)):
    a = A[i]
    b = B[i]
    algebraic_sum.append(a+b-a*b)
    algebraic_product.append(a*b)
    bounded_sum.append(min(1, a+b))
    bounded_difference.append(max(0, a-b))

print("Algebraic sum:", algebraic_sum)
print("Algebraic product:", algebraic_product)
print("Bounded sum:", bounded_sum)
print("Bounded difference:", bounded_difference)

# Cartesian product
A = [0.3, 0.7, 1.0]
B = [0.4, 0.9]
R = []
for a in A:
    row = []
    for b in B:
        row.append(min(a,b))
    R.append(row)
print("Cartesian product:", R)

# Max-min and max-product composition
R = [[0.6,0.3], [0.2,0.9]]
S = [[1.0,0.5,0.3], [0.8,0.4,0.7]]
max_min = []
max_product = []

for i in range(len(R)):
    row_min = []
    row_product = []
    for j in range(len(S[0])):
        values_min = []
        values_product = []
        for k in range(len(S)):
            values_min.append(min(R[i][k], S[k][j]))
            values_product.append(R[i][k]*S[k][j])
        row_min.append(max(values_min))
        row_product.append(max(values_product))
    max_min.append(row_min)
    max_product.append(row_product)

print("Max-min composition:", max_min)
print("Max-product composition:", max_product)

# Theory: Fuzzy sets use membership values from 0 to 1. Operations combine
# memberships, while composition combines fuzzy relations.

# Water Jug Problem using Depth First Search (DFS)

# Read jug capacities and target
a = int(input("Capacity of jug 1: "))
b = int(input("Capacity of jug 2: "))
target = int(input("Target amount: "))

def get_states(x, y):
    # Fill, empty, and pour operations
    return [
        (a,y), (x,b), (0,y), (x,0),
        (x-min(x,b-y), y+min(x,b-y)),
        (x+min(y,a-x), y-min(y,a-x))
    ]

def dfs():
    stack = [(0,0)]
    visited = []

    while stack:
        x,y = stack.pop()
        if (x,y) in visited:
            continue
        visited.append((x,y))
        print(x,y)

        if x == target or y == target:
            print("Target achieved:", x,y)
            return

        for state in get_states(x,y):
            if state not in visited:
                stack.append(state)

    print("No solution found")

dfs()

# Theory: DFS explores one path deeply using a stack before backtracking.
# It finds a solution but does not guarantee the shortest path.

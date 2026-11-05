# Water Jug Problem using Breadth First Search (BFS)
from collections import deque

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

def bfs():
    queue = deque([(0,0)])
    visited = []

    while queue:
        x,y = queue.popleft()
        if (x,y) in visited:
            continue
        visited.append((x,y))
        print(x,y)

        if x == target or y == target:
            print("Target achieved:", x,y)
            return

        for state in get_states(x,y):
            if state not in visited:
                queue.append(state)

    print("No solution found")

bfs()

# Theory: BFS explores states level by level using a queue, finding a
# shortest sequence of jug operations when a solution exists.

# Missionaries and Cannibals Problem using BFS
# State: (missionaries_left, cannibals_left, boat_side)
# boat_side: 0 = left bank, 1 = right bank

from collections import deque

TOTAL_M = 3
TOTAL_C = 3
BOAT_CAPACITY = 2


# Check whether a state is valid and safe
def is_safe(m_left, c_left):
    m_right = TOTAL_M - m_left
    c_right = TOTAL_C - c_left

    if m_left < 0 or c_left < 0:
        return False
    if m_left > TOTAL_M or c_left > TOTAL_C:
        return False

    # Cannibals must not outnumber missionaries on either bank
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False

    return True


# Generate all possible boat crossings
def get_next_states(state):
    m_left, c_left, boat = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    next_states = []

    for m, c in moves:
        if boat == 0:
            new_m = m_left - m
            new_c = c_left - c
            new_boat = 1
        else:
            new_m = m_left + m
            new_c = c_left + c
            new_boat = 0

        # Check the move and resulting state
        if is_safe(new_m, new_c):
            next_states.append((new_m, new_c, new_boat))

    return next_states


# Find a solution using Breadth-First Search
def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        for next_state in get_next_states(current):
            if next_state not in parent:
                parent[next_state] = current
                queue.append(next_state)

    # Reconstruct the path
    if goal not in parent:
        print("No solution found.")
        return

    path = []
    state = goal

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()

    print("Missionaries and Cannibals Solution")
    print("State format: (M left, C left, Boat side)")
    print("Boat: 0 = Left, 1 = Right")
    print()

    for step, state in enumerate(path):
        print("Step", step, ":", state)

    print("\nTotal crossings:", len(path) - 1)


# Run the program
solve()


# Theory:
# State-space search represents each situation as a state and each boat
# crossing as an action. BFS explores states level by level and finds the
# shortest solution. A state is allowed only when missionaries are not
# outnumbered by cannibals on either bank where missionaries are present.

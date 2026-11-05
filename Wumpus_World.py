# Wumpus World - Simple 4x4 Grid

# Place the start, Wumpus, pits, and gold
start = (1, 1)
wumpus = (3, 3)
pits = [(2, 3), (4, 2)]
gold = (4, 4)

# Check whether two cells are next to each other

def adjacent(cell1, cell2):
    row_difference = abs(cell1[0] - cell2[0])
    col_difference = abs(cell1[1] - cell2[1])
    return row_difference + col_difference == 1

# Display percepts sensed by the agent in a cell
def show_percepts(position):
    print("Agent at:", position)

    if adjacent(position, wumpus):
        print("Stench: Wumpus is nearby")

    for pit in pits:
        if adjacent(position, pit):
            print("Breeze: Pit is nearby")

    if position == gold:
        print("Glitter: Gold is here")

    print()

# A simple safe route from the start to the gold
route = [
    (1, 1), (1, 2), (1, 3), (1, 4),
    (2, 4), (3, 4), (4, 4)
]

print("WUMPUS WORLD (4x4)")
print("S = Start, W = Wumpus, P = Pit, G = Gold")

# Print the grid; row 4 is displayed at the top
for row in range(4, 0, -1):
    for col in range(1, 5):
        cell = (row, col)
        symbol = "."
        if cell == start:
            symbol = "S"
        elif cell == wumpus:
            symbol = "W"
        elif cell in pits:
            symbol = "P"
        elif cell == gold:
            symbol = "G"
        print(symbol, end=" ")
    print()

# Move the agent along the route and show its percepts
print("\nAgent movement and percepts:\n")
for position in route:
    if position == wumpus or position in pits:
        print("Agent encountered a hazard!")
        break

    show_percepts(position)

    if position == gold:
        print("Gold collected! Agent wins.")

# Theory:
# Wumpus World is a 4x4 grid-based environment. The agent senses
# stench near the Wumpus, breeze near pits, and glitter at the gold.
# The agent uses these percepts to move safely and collect the gold.

'''
1. Break down the code for the 8 puzzle problem into
smaller piece :
Using BFS:
i. WAF to Check two 8 puzzle are equal or not . If equal
return true else return false.
ii. WAF to find the position of the blank tile present in the
8 puzzle and then return it's position.
iii. WAF to find the new states that generated after making
the shifting the empty tile to one
position(up/down/left/right) and display it.
'''
import copy
from collections import deque

def equal(puzzle1, puzzle2):
    return puzzle1 == puzzle2

def blank(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == 0:
                return (row, col)
    return None

def newState(puzzle):
    newstates = []
    row, col = blank(puzzle)

    moves = {
        "UP": (-1, 0),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
        "RIGHT": (0, 1)
    }

    for move, (mr, mc) in moves.items():
        new_row, new_col = row + mr, col + mc

        if 0 <= new_row < len(puzzle) and 0 <= new_col < len(puzzle[0]):
            new_puzzle = copy.deepcopy(puzzle)
            new_puzzle[row][col], new_puzzle[new_row][new_col] = new_puzzle[new_row][new_col], new_puzzle[row][col]

            newstates.append((new_puzzle, move))

    return newstates  

def eightpuzzle(start, goal):
    """Solve the 8-puzzle using BFS."""
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if equal(current_state, goal):
            return path
        
        state_tuple = tuple(tuple(row) for row in current_state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for new_state, move in newState(current_state):
            queue.append((new_state, path + [move]))  

    return None

start_puzzle = [
    [1, 2, 3],
    [4, 8, 5],
    [7, 0, 6]
]

goal_puzzle = [
    [1, 0, 2],
    [4, 8, 3],
    [7, 6, 5]
]

solution_path = eightpuzzle(start_puzzle, goal_puzzle)

if solution_path:
    print("Solution Found! Moves to solve the puzzle:", solution_path)
else:
    print("No solution found.")

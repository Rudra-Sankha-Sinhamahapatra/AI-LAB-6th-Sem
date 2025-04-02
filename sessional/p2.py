'''
write the function to compute the heuristic value of a 8 puzzle problem shown below
(Note: goal state: 1-8 order , empty tile at end)
[2,8,3]
[1,6,4]
[7,_,5]
'''

def manhattan_distance(state):
    goal = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 2), 5: (2, 2), 6: (1, 1),
        7: (2, 0), 8: (1, 0), '_': (2, 1)
    }
    
    total_distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != '_':  
                goal_x, goal_y = goal[tile]
                total_distance += abs(i - goal_x) + abs(j - goal_y)
    
    return total_distance


given_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, '_', 5]
]

h_value = manhattan_distance(given_state)
print("Heuristic Value (Manhattan Distance):", h_value)

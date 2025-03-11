'''
15 puzzle implementation via A Star Search
'''

import copy
import heapq

goal_puzzle = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]

goal_positions = {num: (r, c) for r, row in enumerate(goal_puzzle) for c, num in enumerate(row)}

def manhattan_distance(puzzle):
    distance = 0
    for r in range(4):
        for c in range(4):
            num = puzzle[r][c]
            if num != 0:
                goal_r, goal_c = goal_positions[num]
                distance += abs(r - goal_r) + abs(c - goal_c)
    return distance

def get_neighbors(puzzle):
    neighbors = []
    zero_r, zero_c = next((r, c) for r in range(4) for c in range(4) if puzzle[r][c] == 0)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        new_r, new_c = zero_r + dr, zero_c + dc
        if 0 <= new_r < 4 and 0 <= new_c < 4:
            new_puzzle = copy.deepcopy(puzzle)
            new_puzzle[zero_r][zero_c], new_puzzle[new_r][new_c] = new_puzzle[new_r][new_c], new_puzzle[zero_r][zero_c]
            neighbors.append(new_puzzle)
    
    return neighbors

def a_star(puzzle):
    heap = []
    heapq.heappush(heap, (manhattan_distance(puzzle), 0, puzzle, []))
    visited = set()
    
    while heap:
        _, cost, current_puzzle, path = heapq.heappop(heap)
        if current_puzzle == goal_puzzle:
            return path
        
        puzzle_tuple = tuple(tuple(row) for row in current_puzzle)
        if puzzle_tuple in visited:
            continue
        visited.add(puzzle_tuple)
        
        for neighbor in get_neighbors(current_puzzle):
            new_path = path + [neighbor]
            heapq.heappush(heap, (cost + 1 + manhattan_distance(neighbor), cost + 1, neighbor, new_path))
    
    return None  # No solution found

start_puzzle = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 0, 12],
    [13, 14, 11, 15]
]

solution = a_star(start_puzzle)
if solution:
    print(f"Solution found in {len(solution)} moves!")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")

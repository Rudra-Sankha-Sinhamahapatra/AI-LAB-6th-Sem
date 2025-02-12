import math
from collections import deque
import heapq

def euclidean_distance(node, goal):
    return math.sqrt((node[1] - goal[1]) ** 2 + (node[2] - goal[2]) ** 2)

def is_goal(node, goal):
    return node == goal

def get_neighbors(graph, node):
    return [neighbor[0] for neighbor in graph.get(node, [])] 

def reconstruct_path(parent, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent.get(goal)
    return path[::-1] 

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], start)) 
    g_score = {start: 0}  
    f_score = {start: heuristic[start]} 
    parent = {start: None}  
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list) 

        if is_goal(current, goal): 
            return reconstruct_path(parent, goal)

        visited.add(current)

        for neighbor in get_neighbors(graph, current):
            if neighbor in visited:
                continue

            tentative_g_score = g_score[current] + next(weight for n, weight in graph[current] if n == neighbor)
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
                parent[neighbor] = current  

    return None  


graph = {
    "A": [("B", 7), ("C", 6)],
    "B": [("D", 4), ("C", 6), ("A", 10)],
    "C": [("E", 5), ("F", 4), ("B", 7), ("A", 10)],
    "D": [("B", 7)],
    "E": [("F", 4), ("C", 6)],
    "F": [("G", 0), ("C", 6), ("E", 5)],
    "G": [("F", 4)]
}

heuristic = {
    "A": 10,
    "B": 7,
    "C": 6,
    "D": 4,
    "E": 5,
    "F": 4,
    "G": 0
}


start = "A"
goal = "G"
path = a_star(graph, start, goal, heuristic)
print(f"Path from {start} to {goal}: {path}")
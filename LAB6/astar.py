
'''
WAP using A* algorithm to find the shortest path from the starting
node A to G for the following graph.
'''

from queue import PriorityQueue

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 3},
    'C': {'E': 5},
    'D': {'F': 2},
    'E': {'G': 3},
    'F': {'G': 1},
    'G': {}
}

heuristic = {
    'A': 5,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 3,
    'F': 1,
    'G': 0
}

def a_star_search(start, goal):
    open_list = PriorityQueue()
    open_list.put((0 + heuristic[start], start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_list.empty():
        _, current = open_list.get()
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                open_list.put((f_score, neighbor))

    return None

path = a_star_search('A', 'G')
print("Shortest path from A to G:", path)

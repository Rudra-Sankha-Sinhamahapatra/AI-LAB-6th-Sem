'''
Write a program to find the path using BFS
for the below mentioned graph. [Hint : create
the Adjacency matrix then use the algorithm
of question one for the path traversal]
'''

from collections import deque

maze =[
    [0, 1, 1, 1],  
    [0, 0, 1, 0],  
    [1, 0, 1, 1],  
    [0, 0, 0, 0], 
]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(*start, [start])])  
    visited = set([start])
    
    while queue:
        x, y, path = queue.popleft()
        if (x, y) == end:
            return path  
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny, path + [(nx, ny)]))
                visited.add((nx, ny))
    return None

start = (0, 0) 
end = (3, 3)  
path = bfs_maze(maze, start, end)

if path:
    print("Path from Source to Destination:", path)
else:
    print("No path found")

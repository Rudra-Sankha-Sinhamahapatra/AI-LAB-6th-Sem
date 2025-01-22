'''
Write a program to find the path using BFS
for the below mentioned graph. [Hint : create
the Adjacency matrix then use the algorithm
of question one for the path traversal]
'''

from collections import deque

graph = [
    [0, 1, 1, 1, 1, 0, 0, 0], 
    [1, 0, 0, 0, 0, 1, 0, 0],  
    [1, 0, 0, 0, 0, 1, 0, 0], 
    [1, 0, 0, 0, 0, 0, 1, 0], 
    [1, 0, 0, 0, 0, 0, 1, 0],  
    [0, 1, 1, 0, 0, 0, 0, 1], 
    [0, 0, 0, 1, 1, 0, 0, 1], 
    [0, 0, 0, 0, 0, 1, 1, 0], 
]

def bfs(graph,start) :
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    path = []

    while queue:
        node = queue.popleft()
        path.append(node + 1)

        for neighbour, connected in enumerate(graph[node]):
            if connected and not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True

    return path


start_node = 0
path = bfs(graph,start_node)
print("BFS Traversal Path:",path)
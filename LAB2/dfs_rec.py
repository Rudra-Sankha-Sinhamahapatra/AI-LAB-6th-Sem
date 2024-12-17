graph = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'C', 'G'],
    'C': ['A', 'B'],
    'D': ['A', 'E'],
    'E': ['A', 'D', 'G', 'F'],
    'F': ['G', 'F'],
    'G': ['B', 'E', 'F'],
}

def dfs_rec(graph, visited, node):
    if node not in visited:
        visited.add(node)
        print(f"Visiting: {node}")
        for adj_ele in graph[node]:
            dfs_rec(graph, visited, adj_ele)


start = 'A'
print("DFS Recursive Traversal:")
visited = set()
dfs_rec(graph, visited, start)
print("Result:", visited)

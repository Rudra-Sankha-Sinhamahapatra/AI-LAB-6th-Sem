import graph

def dfs_rec(graph, visited, node):
    if node not in visited:
        visited.add(node)
        print(f"Visiting: {node}")
        for adj_ele in graph[node]:
            dfs_rec(graph, visited, adj_ele)


start = 'A'
print("DFS Recursive Traversal:")
visited = set()
dfs_rec(graph.graph, visited, start)
print("Result:", visited)

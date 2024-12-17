def dfs(graph, start):
    visited = set()              
    stack = [start]               
    
    while stack:
        node = stack.pop()         
        if node not in visited:   
            print(f"Visiting: {node}")
            visited.add(node)      
            
            neighbors = sorted(graph[node], reverse=True)
            stack.extend(neighbors)
    return visited


graph = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'C', 'G'],
    'C': ['A', 'B'],
    'D': ['A', 'E'],
    'E': ['A', 'D', 'G', 'F'],
    'F': ['G', 'F'],
    'G': ['B', 'E', 'F'],
}


print("DFS Traversal:")
visited_nodes = dfs(graph, 'A')
print("Result:", visited_nodes)

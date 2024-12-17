import graph

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


print("DFS Traversal:")
visited_nodes = dfs(graph.graph, 'A')
print("Result:", visited_nodes)

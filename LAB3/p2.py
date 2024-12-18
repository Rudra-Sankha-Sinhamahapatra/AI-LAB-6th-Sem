matrix = [
    [0,0,0,1,0],
    [1,0,0,0,1],
    [0,1,0,0,1],
    [0,0,1,0,1],
    [0,1,1,0,0]
]

# write a program in python to find the neighbouring elements of each element present in the below adjacency matrix (0 represents no connection of element and 1 represent connection between adjacency element).After finding the element put the same into a dictionary and then apply dfs for traversing the element

def matrix_to_dict(matrix):
      neighbours = {}
      for i in range(len(matrix)):
         neighbours[i] = []
         for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                neighbours[i].append(j)
      return neighbours

def dfs(graph,start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(f"Visited : {node}")
            visited.add(node)
            stack.extend((graph[node]))
    return visited

graph_dict = matrix_to_dict(matrix)
print("Graph Dictionary: ",graph_dict)

visited_nodes = dfs(graph_dict,1)
print("Visited nodes:",visited_nodes)
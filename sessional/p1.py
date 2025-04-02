'''
Write a program to search a path start to end point 
in a 2D grid using the recursive DFS Algorithm and 
then display the path
'''

def dfs(grid, x, y, end_x, end_y, path, visited):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 1 or (x, y) in visited:
        return False
    
    path.append((x, y))
    visited.add((x, y))
    
    if (x, y) == (end_x, end_y):
        return True
    

    if (dfs(grid, x + 1, y, end_x, end_y, path, visited) or
        dfs(grid, x - 1, y, end_x, end_y, path, visited) or
        dfs(grid, x, y + 1, end_x, end_y, path, visited) or
        dfs(grid, x, y - 1, end_x, end_y, path, visited)):
        return True
    
    path.pop()
    return False

def find_path(grid, start, end):
    path = []
    visited = set()
    if dfs(grid, start[0], start[1], end[0], end[1], path, visited):
        return path
    return "No path found"


grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = find_path(grid, start, end)
print("Path:", path)
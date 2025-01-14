def solve_maze_iterative(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [start]  
    visited = set() 
    parent = {}     

    while stack:
        position = stack.pop()
        x, y = position

     
        if position == end:
            path = []
            while position:
                path.append(position)
                position = parent.get(position)
            return path[::-1] 

    
        if position not in visited:
            visited.add(position)

          
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                    stack.append((nx, ny))
                    parent[(nx, ny)] = position

    return None 



maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)


path = solve_maze_iterative(maze, start, end)
if path:
    print("Path found using iterative method:", path)
else:
    print("No path exists.")

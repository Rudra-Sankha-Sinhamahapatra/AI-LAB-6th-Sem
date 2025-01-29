def dfs(position,rows,cols,visited,path):
    x, y = position
   
    if position == end:
        path.append(position)
        return True

  
    visited.add(position)

   
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
      
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
            if dfs((nx, ny),rows,cols,visited,path): 
                path.append(position) 
                return True

    return False


def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    path = []

    def dfs(pos):
        x, y = pos
        if pos == end:
            path.append(pos)
            return True

     
        visited.add(pos)
        path.append(pos)

        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
          
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                if dfs((nx, ny)):  
                    return True

        
        path.pop()
        return False

    if dfs(start):
        return path
    else:
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


path = solve_maze(maze, start, end)
if path:
    print("Path found:", path)
else:
    print("No path exists.")

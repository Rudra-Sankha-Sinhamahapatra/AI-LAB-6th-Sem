def dfs(position,rows,cols,visited,path):
    x, y = position
    # Base Case: Reached the end
    if position == end:
        path.append(position)
        return True

    # Mark the current cell as visited
    visited.add(position)

    # Explore all possible directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Check if the move is valid
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
            if dfs((nx, ny),rows,cols,visited,path):  # Recursive DFS call
                path.append(position)  # Add to path if successful
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

        # Mark as visited
        visited.add(pos)
        path.append(pos)

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            # Check bounds and validity
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                if dfs((nx, ny)):  # Recursive call
                    return True

        # Backtrack
        path.pop()
        return False

    if dfs(start):
        return path
    else:
        return None

# Example Maze
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Starting point
end = (4, 4)    # Ending point

# Solve the maze
path = solve_maze(maze, start, end)
if path:
    print("Path found:", path)
else:
    print("No path exists.")

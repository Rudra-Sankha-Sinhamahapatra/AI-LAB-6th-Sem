def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    path = []  # Store the path
    visited = set()  # Track visited cells

    def dfs(pos):
        x, y = pos

        # Check if we reached the destination
        if pos == end:
            path.append(pos)
            return True

        # Check if the position is out of bounds, blocked, or already visited
        if not (0 <= x < rows and 0 <= y < cols) or maze[x][y] == 1 or pos in visited:
            return False

        # Mark the position as visited
        visited.add(pos)
        path.append(pos)

        # Explore all possible directions (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if dfs((x + dx, y + dy)):
                return True

        # Backtrack: Remove the position from the path
        path.pop()
        return False

    # Start the DFS traversal
    if dfs(start):
        return path
    return None

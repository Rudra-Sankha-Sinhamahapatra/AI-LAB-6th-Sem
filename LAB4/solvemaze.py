def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    path = [] 
    visited = set()  

    def dfs(pos):
        x, y = pos


        if pos == end:
            path.append(pos)
            return True

        if not (0 <= x < rows and 0 <= y < cols) or maze[x][y] == 1 or pos in visited:
            return False


        visited.add(pos)
        path.append(pos)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if dfs((x + dx, y + dy)):
                return True

        path.pop()
        return False

    if dfs(start):
        return path
    return None

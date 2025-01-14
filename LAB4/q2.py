from solvemaze import solve_maze

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
    print("Path found after altering values:", path)
else:
    print("No path exists.")

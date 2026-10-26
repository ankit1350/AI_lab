# Maze Solving using Depth-First Search (DFS)
# 0 = Open Path
# 1 = Wall

maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]

rows = len(maze)
cols = len(maze[0])

visited = set()
path = []

def dfs(x, y):
    # Check boundaries
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return False

    # Check wall and visited cells
    if maze[x][y] == 1 or (x, y) in visited:
        return False

    visited.add((x, y))
    path.append((x, y))

    print("Visited:", (x, y))

    # Goal test
    if (x, y) == (3, 3):
        return True

    # Explore neighbors: down, up, right, left
    if dfs(x + 1, y):
        return True

    if dfs(x - 1, y):
        return True

    if dfs(x, y + 1):
        return True

    if dfs(x, y - 1):
        return True

    # Backtrack if the goal is not found
    path.pop()
    return False


print("Starting DFS from (0, 0)\n")

if dfs(0, 0):
    print("\nGoal Reached!")
    print("Path:", path)
    print("Path Length:", len(path) - 1)
else:
    print("\nNo Path Exists.")
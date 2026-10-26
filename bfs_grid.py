from collections import deque

# 0 = Free cell, 1 = Obstacle
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

# Initialize BFS
queue = deque([start])
visited = {start}
parent = {start: None}

# Down, up, right, left
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# BFS search
while queue:
    current = queue.popleft()
    print("Visited:", current)

    # Check whether the goal is reached
    if current == goal:
        break

    x, y = current

    # Explore neighboring cells
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        neighbor = (nx, ny)

        if (
            0 <= nx < len(grid)
            and 0 <= ny < len(grid[0])
            and grid[nx][ny] == 0
            and neighbor not in visited
        ):
            visited.add(neighbor)
            parent[neighbor] = current
            queue.append(neighbor)

# Reconstruct the shortest path
if goal in visited:
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("\nShortest Path:", path)
    print("Goal Reached!")
else:
    print("\nNo Path Exists.")
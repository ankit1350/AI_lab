from collections import deque

grid = [
    ['S', '.', '.', '#', '.'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', 'G']
]

ROWS = len(grid)
COLS = len(grid[0])

start = (0, 0)
goal = (4, 4)


class ModelBasedAgent:
    def __init__(self, start, goal):
        self.position = start
        self.goal = goal
        self.internal_map = {}
        self.visited = set()
        self.path = [start]

    def perceive(self, grid):
        r, c = self.position

        directions = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }

        self.internal_map[(r, c)] = grid[r][c]

        for dr, dc in directions.values():
            nr = r + dr
            nc = c + dc

            if 0 <= nr < ROWS and 0 <= nc < COLS:
                self.internal_map[(nr, nc)] = grid[nr][nc]

    def find_path(self):
        queue = deque([(self.position, [self.position])])
        visited = {self.position}

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            current, path = queue.popleft()

            if current == self.goal:
                return path

            r, c = current

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                next_cell = (nr, nc)

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and next_cell not in visited
                    and self.internal_map.get(next_cell, '#') != '#'
                ):
                    visited.add(next_cell)
                    queue.append((next_cell, path + [next_cell]))

        return None

    def move(self, next_position):
        self.position = next_position
        self.visited.add(next_position)
        self.path.append(next_position)

    def run(self, grid):
        self.visited.add(self.position)

        while self.position != self.goal:
            # Observe the current cell and its neighbors
            self.perceive(grid)

            # Plan a path using the known map
            path = self.find_path()

            if path is None:
                # Explore an unvisited, known open neighbor
                r, c = self.position
                moved = False

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    neighbor = (nr, nc)

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] != '#'
                        and neighbor not in self.visited
                    ):
                        self.move(neighbor)
                        moved = True
                        break

                if not moved:
                    print("No path to goal found.")
                    return

            else:
                if len(path) < 2:
                    break

                self.move(path[1])

            print("Current Position:", self.position)

        print("\nGoal Reached!")
        print("Complete Path:", self.path)
        print("Visited Cells:", self.visited)


print("Grid Environment:")
for row in grid:
    print(" ".join(row))

agent = ModelBasedAgent(start, goal)
agent.run(grid)
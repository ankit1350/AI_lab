'''The Tower of Hanoi consists of:
Three rods: A, B, and C.
Disks: Disks of different sizes stacked on rod A.
Objective: Move all disks from rod A to rod C.

Rules
Move only one disk at a time.
Only the top disk of a rod can be moved.
A larger disk cannot be placed on top of a smaller disk.'''

from collections import deque

def get_successors(state):
    successors=[]
    pegs=[list(peg) for peg in state]  # converts peg fromm tuple to list 
    # identify source peg
    for source in range(3):
        if not pegs[source]:
            continue

        disk = pegs[source][-1]

        for destination in range(3):
            if source == destination:
                continue
            if not pegs[destination] or pegs[destination][-1] > disk:
                new_pegs = [peg[:] for peg in pegs]

                new_pegs[source].pop()
                new_pegs[destination].append(disk)
                new_state = tuple(tuple(peg) for peg in new_pegs)
                successors.append((new_state, source, destination, disk))                
    return successors                
def tower_of_hanoi_bfs(n):
    initial = (tuple(range(n, 0, -1)), (), ())
    goal = ((), (), tuple(range(n, 0, -1)))
    queue = deque()
    queue.append((initial, []))

    visited = {initial}
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal:
            return path
        for next_state, source, destination, disk in get_successors(current_state):
            if next_state not in visited:
                visited.add(next_state)
                move = (
                    f"Move disk {disk} from "
                    f"{chr(65 + source)} to {chr(65 + destination)}"
                )
                queue.append((next_state, path + [move]))
    return None
n = int(input("Enter number of disks: "))
solution = tower_of_hanoi_bfs(n)

if solution:
    print("\nSolution using State Space Search:\n")

    for i, move in enumerate(solution, start=1):
        print(f"Step {i}: {move}")

    print("\nTotal moves:", len(solution))
else:
    print("No solution found.")
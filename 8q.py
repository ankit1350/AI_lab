N = 8

board = [[0 for _ in range(N)] for _ in range(N)]


# Check whether a position is safe
def is_safe(row, col):

    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Solve using backtracking
def solve(row):

    # All queens placed successfully
    if row == N:
        return True

    # Try every column
    for col in range(N):

        if is_safe(row, col):

            board[row][col] = 1

            if solve(row + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Execute the program
if solve(0):

    print("Solution Found!")

    for row in board:
        for cell in row:
            if cell == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

else:
    print("No solution exists.")
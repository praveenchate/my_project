def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if board[i] - i == col - row:
            return False
        if board[i] + i == col + row:
            return False
    return True

def solve_n_queen(board, row, n):
    if row == n:
        print_board(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queen(board, row + 1, n)


n = 4
board = [-1] * n

print(f"Solutions for {n}-Queen Problem:\n")
solve_n_queen(board, 0, n)
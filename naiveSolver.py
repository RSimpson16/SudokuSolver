def is_valid(board, row, col, num):
    # Check if the number is already in the current row
    if num in board[row]:
        return False

    # Check if the number is already in the current column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is already in the current 3x3 sub-grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    # Find an empty cell
    empty_cell = find_empty_cell(board)

    # If no empty cells are found, the Sudoku is solved
    if not empty_cell:
        return True

    row, col = empty_cell

    # Try each number from 1 to 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            # Recursively attempt to solve the rest of the board
            if solve_sudoku(board):
                return True

            # If no solution was found, backtrack
            board[row][col] = 0

    # If no number from 1 to 9 works in this cell, return False to backtrack
    return False


def find_empty_cell(board):
    # Find the first empty cell (represented by 0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def print_board(board):
    for row in board:
        print(row)


# Example Sudoku board (0 represents empty cells)
board = [
    [0, 6, 8, 0, 2, 4, 9, 0, 0],
    [3, 4, 0, 5, 1, 0, 0, 8, 7],
    [1, 0, 7, 3, 8, 0, 0, 5, 0],
    [0, 8, 5, 0, 3, 1, 4, 7, 0],
    [2, 1, 9, 0, 0, 7, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 2],
    [4, 7, 3, 6, 0, 0, 0, 9, 1],
    [0, 0, 0, 0, 0, 0, 0, 4, 0],
    [8, 0, 0, 0, 0, 3, 0, 0, 6]
]

print("Original Sudoku:")
print_board(board)

if solve_sudoku(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("\nNo solution exists.")

def is_valid(board, row, col, num):
    # Check if the current row does not contain the number
    if num in board[row]:
        return False
    
    # Check if the current column does not contain the number
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the current 3x3 subgrid does not contain the number
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        else:
                            board[i][j] = 0
                return False
    return True

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
            if (j + 1) % 3 == 0 and j < 8:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0 and i < 8:
            print("-" * 21)

# Example Sudoku puzzle (0 represents empty cells)
input_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(input_board):
    print("Sudoku Solved Successfully:")
    print_board(input_board)
else:
    print("No solution exists.")

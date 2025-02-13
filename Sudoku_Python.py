import random

def get_random_digit(min_val, max_val):
    return random.randint(min_val, max_val)

def is_valid(board, row, col, num):
    num = str(num)
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    curr_row, curr_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[curr_row + i][curr_col + j] == num:
                return False
    return True

def backtrack_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                nums = list('123456789')
                random.shuffle(nums)
                for num in nums:
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if backtrack_sudoku(board):
                            return True
                        board[i][j] = '.'
                return False
    return True

def remove_digits(board):
    counter = get_random_digit(40, 50)
    while counter > 0:
        row, col = get_random_digit(0, 8), get_random_digit(0, 8)
        if board[row][col] == '.':
            continue
        board[row][col] = '.'
        counter -= 1

def generate_random_sudoku():
    board = [['.' for _ in range(9)] for _ in range(9)]
    backtrack_sudoku(board)
    remove_digits(board)
    return board

def solve_sudoku(board):
    def solving(i, j):
        if i == 9:
            return True
        if j == 9:
            return solving(i + 1, 0)
        if board[i][j] != '.':
            return solving(i, j + 1)
        
        for num in map(str, range(1, 10)):
            if is_valid(board, i, j, num):
                board[i][j] = num
                if solving(i, j + 1):
                    return True
                board[i][j] = '.'
                
        return False
    
    solving(0, 0)

def display(board):
    for row in board:
        print(" ".join(row))

def main():
    test_board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]
    
    print("Testing Sudoku Board 1:")
    display(test_board)
    
    print("\nSolving Sudoku Board 1:")
    solve_sudoku(test_board)
    display(test_board)
    
    print("\nTesting Random Sudoku Board:")
    test_board2 = generate_random_sudoku()
    display(test_board2)
    
    print("\nSolving Random Sudoku Board:")
    solve_sudoku(test_board2)
    display(test_board2)

if __name__ == "__main__":
    main()

"""
Sudoku
---
Check if the number is not repeat in a column
Check if the number is not repeat in a row
Check if the number is not repeat in a box
"""

def check_is_not_row(matrix, row, num):
    for i in range(9):
        if matrix[row][i] == num : 
            return False
    return True

def check_is_not_column(matrix, col, num):
    for i in range(9):
        if matrix[col][i] == num : 
            return False
    return True

def check_is_not_box(matrix, row, col, num):
    for i in range(3):
        for j in range(3):
            if matrix[row+i][col+i] == num : 
                return False
    return True

def check_if_is_correct(matrix, row, col, num):
    return check_is_not_column(matrix, col, num) and check_is_not_row(matrix, row, num) and check_is_not_box(matrix, row - row % 3, col - col % 3, num)

def main():
    grid = [[3, 1, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 4, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 4, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 3, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 9, 4, 7, 2, 5, 6],
    [6, 9, 2, 3, 5, 1, 8, 7, 4],
    [7, 4, 5, 2, 8, 6, 3, 1, 9]]

    for i in range (0,9):
        for j in range (0,9):
            if check_if_is_correct(grid, i, j , grid[i][j]):
                continue
            else :
                print("Mala solucion")


if __name__ == "__main__":
    main()
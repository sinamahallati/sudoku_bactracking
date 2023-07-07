'''We’ll use the backtracking method to create our sudoku solver in Python.
Backtracking means switching back to the previous step as soon as we 
determine that our current solution cannot be continued into a complete one.'''

#We use this principle of backtracking to implement the sudoku algorithm
#In this method for solving the sudoku puzzle, first, we assign the size of the 2D matrix to a variable M (M*M).

M = 9
def puzzle(a):
    '''  we assign the utility function (puzzle) to print the grid.
        it will assign num to the row and col.
    '''
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, row, col, num):
    ''' If we find the same num in the same row or same column
    or in the specific 3*3 matrix,
    false will be returned. '''
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 # Then we will check if we have reached the 8th row and 9th column and return true for stopping further backtracking.
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def Suduko(grid, row, col):
    '''  check if the column value becomes 9 
    then we move to the next row and column.'''

    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:# if the current position of the grid has a value greater than 0, then we iterate for the next column.
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
# After checking if it is a safe place, we move to the next column and then assign the num in the current (row, col) position of the grid. Later we check for the next possibility with the next column.
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
#0 means the cells where no value is assigned

# Example input 
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]]

# Running the code and Print the results

if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist:(")

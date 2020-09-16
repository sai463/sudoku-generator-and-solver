from sudoku_generator import MakeSudoku

def find_empty(arr,l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False

def used_in_row(arr,row,num):
    for i in range(9):
        if(arr[row][i]==num):
            return True
    return False

def used_in_col(arr,col,num):
    for i in range(9):
        if (arr[i][col] == num):
            return True
    return False

def used_in_box(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if (arr[i+row][j+col]==num):
                return True
    return False

def check_location(arr,row,col,num):
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row-row%3,col-col%3,num)

def solve_sudoku(arr):
    l=[0,0]
    if(not find_empty(arr,l)):
        return True
    row=l[0]
    col=l[1]

    for num in range(1,10):
        if(check_location(arr,row,col,num)):
            arr[row][col]=num
            if(solve_sudoku(arr)):
                return True
            arr[row][col]=0
    return False

if __name__=="__main__":
    grid=[[0 for x in range(9)] for y in range(9)]
    grid=MakeSudoku()
#you can use your own sudoku set by making changes in the following matrix and commenting the import line
    """   
        grid=[
            [5, 0, 0, 6, 2, 0, 7, 0, 0],
            [3, 6, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 4, 6, 9],
            [6, 0, 0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 7, 8, 0, 0, 0, 0, 0],
            [0, 1, 0, 7, 4, 5, 0, 0, 6],
            [8, 3, 5, 2, 0, 0, 0, 4, 0],
            ]
    """

    print("Before solving....")
    for i in range(len(grid)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(grid[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(grid[i][j])+" "
        print(line)

    if(solve_sudoku(grid)):
        print('\n')
        print("After solving....")
        for i in range(len(grid)):
            line = ""
            if i == 3 or i == 6:
                print("---------------------")
            for j in range(len(grid[i])):
                if j == 3 or j == 6:
                    line += "| "
                line += str(grid[i][j]) + " "
            print(line)
    else:
        print("\n")
        print("no solution for this")



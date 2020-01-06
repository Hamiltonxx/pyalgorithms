# Backtracking is an algorithmic paradigm that tries different solutions until finds a solution that "works".

### The Knight's tour problem ###
n = 8 # Chessboard Size

def isSafe(x,y,board):
    if 0<=x<n and 0<=y<n and board[x][y]==-1:
        return True 
    return False 

def printSolution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")
        print()

def solveKT():
    board = [[-1 for i in range(n)] for j in range(n)]
    move_x = [2, 1,-1,-2,-2,-1, 1, 2]
    move_y = [1, 2, 2, 1,-1,-2,-2,-1]
    board[0][0] = 0
    pos = 1
    if not solveKTUtil(board,0,0,move_x,move_y,pos):
        print("Solution does not exist")
    else:
        printSolution(board)

def solveKTUtil(board,curr_x,curr_y,move_x,move_y,pos):
    if pos==n**2:
        return True
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if isSafe(new_x,new_y,board):
            board[new_x][new_y] = pos
            if solveKTUtil(board,new_x,new_y,move_x,move_y,pos+1):
                return True
            # Backtracking
            board[new_x][new_y] = -1
    return False

if __name__ == '__main__':
    solveKT()
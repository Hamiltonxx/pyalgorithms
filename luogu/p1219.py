N = int(input())

board = [[0]*N for _ in range(N)]

def isAttack(i,j):
    for k in range(N):
        if board[i][k]==1 or board[k][j]==1:
            return True 
    for k in range(N):
        for l in range(N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True 
    return False 

def nQueen(n):
    if n==0:
        return True 
    for i in range(N):
        for j in range(N):
            if not isAttack(i,j) and board[i][j]!=1:
                board[i][j] = 1 
                if nQueen(n-1):
                    return True 
                board[i][j] = 0
    return False 

nQueen(N)
for i in board:
    print(i)
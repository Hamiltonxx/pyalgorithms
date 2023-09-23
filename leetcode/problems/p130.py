from itertools import product,chain
def solve(board):
    m, n = len(board), len(board[0])
    def dfs(i,j):
        board[i][j] = '1'
        for r,c in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            if 0<=r<m and 0<=c<n and board[r][c]=='O':
                dfs(r,c)
    for i,j in chain(product(range(m),[0,n-1]), product([0,m-1],range(n))):
        if board[i][j] == 'O':
            dfs(i,j)

    for i,j in product(range(m),range(n)):
        if board[i][j] == 'O': board[i][j] = 'X'
        elif board[i][j] == '1': board[i][j] = 'O'


def solveSET(board):
    m, n = len(board), len(board[0])
    seen = set()
    def dfs(i,j):
        seen.add((i,j))
        for r,c in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            if 0<=r<m and 0<=c<n and (r,c) not in seen and board[r][c]=='O':
                dfs(r,c)
    for i,j in chain(product(range(m),[0,n-1]), product([0,m-1],range(n))):
        if board[i][j] == 'O':
            dfs(i,j)
    for i,j in product(range(m),range(n)):
        if (i,j) not in seen:
            board[i][j] = 'X'
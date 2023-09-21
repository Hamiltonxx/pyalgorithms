from itertools import product, chain
def numEnclaves(grid):
    m,n = len(grid),len(grid[0])
    def dfs(i,j):
        grid[i][j] = 0
        for r,c in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            if 0<=r<m and 0<=c<n and grid[r][c]:
                dfs(r,c)
    for i,j in chain(product(range(m),[0,n-1]), product([0,m-1],range(n))):
        if grid[i][j]:
            dfs(i,j)
    return sum(chain(*grid))

def maxsafe(grid):
    n = len(grid)
    def dfs(grid,i=0,j=0):
        if grid[i][j]:
            return 0
        if i<n and j<n:
            return max(grid)


from functools import lru_cache
def maxAreaOfIslands(grid):
    m, n = len(grid), len(grid[0])
    # @lru_cache(None) #加上cache就是WA,why?
    def dfs(i,j):
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
            return 0
        grid[i][j] = 0
        return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
    mx = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                mx = max(mx, dfs(i,j))
    return mx
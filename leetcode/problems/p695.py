# from functools import lru_cache
# def maxAreaOfIslands(grid):
#     m, n = len(grid), len(grid[0])
#     # @lru_cache(None) #加上cache就是WA,why?
#     def dfs(i,j):
#         if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
#             return 0
#         grid[i][j] = 0
#         return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
#     mx = 0
#     for i in range(m):
#         for j in range(n):
#             if grid[i][j] == 1:
#                 mx = max(mx, dfs(i,j))
#     return mx

from itertools import chain
def maxAreaOfIslands(grid):
    m, n = len(grid), len(grid[0])
    mn = m * n 
    p = list(range(mn))
    size = list(chain(*grid))

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    def union(x,y):
        xroot,yroot = find(x),find(y)
        if xroot != yroot:
            p[xroot] = yroot
            size[yroot] += size[xroot]
    
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                idx = i * n + j
                if j<n-1 and grid[i][j+1]:
                    union(idx+1, idx)
                if i<m-1 and grid[i+1][j]:
                    union(idx+n, idx)

    return max(size)

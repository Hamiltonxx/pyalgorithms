# grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
# ones = []

# n = len(grid)
# for i in range(n):
#     for j in range(n):
#         if grid[i][j]:
#             ones.append((i,j))

# while i<n and j<n:

def maxsafe(grid):
    n = len(grid)
    def dfs(grid,i=0,j=0):
        if grid[i][j]:
            return 0
        if i<n and j<n:
            return max(grid)


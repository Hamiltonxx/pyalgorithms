# def islandPerimeter(grid):
#     m, n = len(grid), len(grid[0])
#     new = [[0]*(n+2)]
#     for row in grid:
#         new.append([0]+row+[0])
#     new.append([0]*(n+2))
#     m, n = m+2, n+2
#     ansx = ansy = 0
#     for i in range(1,m):
#         for j in range(1,n):
#             if new[i][j] != new[i][j-1]:
#                 ansy += 1
#     for j in range(1,n):
#         for i in range(1,m):
#             if new[i][j] != new[i-1][j]:
#                 ansx += 1
#     return ansx + ansy

def islandPerimeter(grid):
    m, n = len(grid), len(grid[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                ans += 4
                if i>0 and grid[i-1][j]:
                    ans -= 2
                if j>0 and grid[i][j-1]:
                    ans -= 2
    return ans
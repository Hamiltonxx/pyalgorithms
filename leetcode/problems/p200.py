
def numIslands(grid):
    m, n = len(grid), len(grid[0])
    cnt = 0
    def dfs(i,j):
        grid[i][j] = 0
        for r,c in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            if 0<=r<m and 0<=c<n and grid[r][c]=='1':
                dfs(r,c)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(i,j)
                cnt += 1
    return cnt

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# print(numIslands(grid))

from collections import deque
def numIslandsbfs(grid):
    m, n = len(grid), len(grid[0])
    cnt = 0
    q = deque([])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                grid[i][j] = 0
                q.append((i,j))
                while q: # turn adj '1' to 0
                    I,J = q.popleft()
                    for r,c in (I+1,J),(I-1,J),(I,J+1),(I,J-1):
                        if 0<=r<m and 0<=c<n and grid[r][c]=='1':
                            grid[r][c] = 0
                            q.append((r,c))
                cnt += 1
    return cnt
                
from itertools import chain
def numIslandsUF(grid):
    m, n = len(grid), len(grid[0])
    cnt = list(chain(*grid)).count('1')
    parent = list(range(m*n))

    def find(x):
        if parent[x] != x:
            return find(parent[x])
        return parent[x]
    def union(x,y):
        nonlocal cnt
        xroot,yroot = find(x),find(y)
        if xroot != yroot:
            parent[xroot] = yroot
            cnt -= 1
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                idx = i*n + j
                if j < n-1 and grid[i][j+1] == '1':
                    union(idx, idx+1)
                if i < m-1 and grid[i+1][j] == '1':
                    union(idx, idx+n)

    return cnt

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslandsUF(grid))
    

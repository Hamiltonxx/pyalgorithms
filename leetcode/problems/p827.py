from itertools import chain
def largestIsland(grid):
    n = len(grid)
    p = list(range(n*n))
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

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                idx = i * n + j
                if j<n-1 and grid[i][j+1]:
                    union(idx+1, idx)
                if i<n-1 and grid[i+1][j]:
                    union(idx+n, idx)

    mx = max(size)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                cur = 1
                seen = set()
                for r,c in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                    if 0<=r<n and 0<=c<n and grid[r][c]:
                        root = find(r * n + c)
                        if root not in seen:
                            seen.add(root)
                            cur += size[root]
                mx = max(mx, cur)
    return mx

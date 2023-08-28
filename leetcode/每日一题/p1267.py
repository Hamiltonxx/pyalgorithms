def countServer(grid):
    rows = [sum(x) for x in grid]
    cols = [sum(y) for y in zip(*grid)]

    n,m = len(grid), len(grid[0])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] and (rows[i]>1 or cols[j]>1):
                cnt += 1
    return cnt

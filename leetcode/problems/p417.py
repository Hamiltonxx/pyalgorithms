from itertools import chain, product
def pacificAtlantic(heights):
    m, n = len(heights), len(heights[0])
    po, ao = set(), set()
    def dfs(i,j,ocean):
        ocean.add((i,j))
        for r,c in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            if 0<=r<m and 0<=c<n and (r,c) not in ocean and heights[r][c]>=heights[i][j]:
                dfs(r,c,ocean)
    for i in range(m):
        dfs(i,0,po)
        dfs(i,n-1,ao)
    for j in range(n):
        dfs(0,j,po)
        dfs(m-1,j,ao)
    return list(po & ao)

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlantic(heights))  


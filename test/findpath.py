from collections import deque

maze = [[1,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1]]

def findpath(maze, start, end):
    rows,cols = len(maze),len(maze[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    q = deque([(*start,0)])
    visited = [[False]*cols for _ in range(rows)]
    visited[start[0]][start[1]] = True
    while q:
        r,c,d = q.popleft()
        if (r,c) == end:
            return d
        for dir in dirs:
            nr,nc = r+dir[0],c+dir[1]
            if 0<=nr<rows and 0<=nc<cols and not visited[nr][nc] and maze[nr][nc]!=0:
                q.append((nr,nc,d+1))
                visited[nr][nc] = True
    return -1

print(findpath(maze,(0,0),(3,3)))
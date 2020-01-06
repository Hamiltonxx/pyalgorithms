N,M,T = map(int,input().split())
sx,sy,fx,fy = map(int,input().split())

maze = [[0]*M for _ in range(N)]

for _ in range(T):
    ox,oy = map(int,input().split())
    maze[ox-1][oy-1] = 1

def backtrack(i,j):
    if i==fx-1 and j==fy-1:
        global n 
        n +=1 
        return
    maze[i][j] = 2
    if j<M-1 and maze[i][j+1]==0:
        backtrack(i,j+1)
    if i<N-1 and maze[i+1][j]==0:
        backtrack(i+1,j)
    if j>0 and maze[i][j-1]==0:
        backtrack(i,j-1)
    if i>0 and maze[i-1][j]==0:
        backtrack(i-1,j)

    maze[i][j]=0


n = 0
backtrack(sx-1,sy-1)
print(n)
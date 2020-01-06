maze = [[0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
row = col = 6

def countPath(i,j,count):
    if i==row-1 and j==col-1:
        count += 1
    else:
        maze[i][j]=2
        if j<col-1 and maze[i][j+1]==0:
            count = countPath(i,j+1,count)
        if i<row-1 and maze[i+1][j]==0:
            count = countPath(i+1,j,count)
        if j>0 and maze[i][j-1]==0:
            count = countPath(i,j-1,count)
        if i>0 and maze[i-1][j]==0:
            count = countPath(i-1,j,count)
        maze[i][j]=0
    return count

print(countPath(0,0,0))

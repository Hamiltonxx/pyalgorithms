maze = [[0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
row = col = 6

count = 0
def countPath(i,j):
    if i<0 or j<0 or i>=row or j>=col or maze[i][j]:
        return 
    if i==row-1 and j==col-1:
        global count 
        count += 1
    else:
        maze[i][j] = 2
        countPath(i,j+1)
        countPath(i+1,j)
        countPath(i,j-1)
        countPath(i-1,j)
        maze[i][j] = 0

countPath(0,0)
print(count)
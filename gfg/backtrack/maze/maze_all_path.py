maze = [[0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
row = col = 6

def findPath(i,j,path):
    if i<0 or j<0 or i>=row or j>=col or maze[i][j]:
        return 
    path.append((i,j))

    if i==row-1 and j==col-1:
        print(path)
    else:
        maze[i][j] = 2
        findPath(i,j+1,path)
        findPath(i+1,j,path)
        findPath(i,j-1,path)
        findPath(i-1,j,path)
        maze[i][j] = 0

    path.pop()

if __name__ == '__main__':
    findPath(0,0,[])
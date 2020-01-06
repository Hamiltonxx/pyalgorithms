maze = [[0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
row = col = 6

def findPath(maze,i,j,path):
    if i==row-1 and j==col-1:
        path.append((i,j))
        print(path)
        return path
    maze[i][j] = 2
    path.append((i,j))
    # l = len(path)
    if j<col-1 and maze[i][j+1]==0:
        path = findPath(maze,i,j+1,path)
    if i<row-1 and maze[i+1][j]==0:
        path = findPath(maze,i+1,j,path)
    if j>0 and maze[i][j-1]==0:
        path = findPath(maze,i,j-1,path)
    if i>0 and maze[i-1][j]==0:
        path = findPath(maze,i-1,j,path)

    maze[i][j] = 0
    # path = path[:l]
    path.pop()

    return path

findPath(maze,0,0,[])
# print(paths)
# print(findPath(maze,0,0,[],[])[1])

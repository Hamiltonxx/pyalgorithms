# maze = [[0,0,1,1,1,1],
#         [1,0,0,0,1,1],
#         [0,0,0,1,0,0],
#         [0,0,0,1,0,1],
#         [1,0,0,0,0,0],
#         [0,0,0,0,1,0]]
maze = [[0,0,1,1],
        [1,0,0,1],
        [0,0,1,1],
        [1,0,0,0]]

# problem: print the path
def findPath(r,c,path=[]):
    if r==3 and c==3:
        path.append((r,c))
        print(path)
        return path
    elif maze[r][c]==0:
        path.append((r,c))
        maze[r][c]=2

    if c<3 and maze[r][c+1]==0:
        path = findPath(r,c+1,path)
    if r<3 and maze[r+1][c]==0:
        path = findPath(r+1,c,path)
    if c>0 and maze[r][c-1]==0:
        path = findPath(r,c-1,path)
    if r>0 and maze[r-1][c]==0:
        path = findPath(r-1,c,path)

    path.pop()
    return path

findPath(0,0)
# print(mypath)


maze = [[0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
# maze = [[0, 0, 1, 1, 1, 1],
#         [1, 0, 0, 0, 1, 1],
#         [0, 0, 0, 1, 0, 0],
#         [0, 0, 0, 1, 0, 1],
#         [1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0]]

# maze = [[0,0,1],
#         [1,0,1],
#         [1,0,0]]

# n=5
# def findPath(r,c):
#     if r==n-1 and c==n-1:
#         return [(n-1,n-1)]
#     if maze[r][c]==0:
#         maze[r][c] = 2

#         if c<n-1 and maze[r][c+1]==0:
#             for item in findPath(r,c+1):
#                 yield [(r,c)]+item #findPath(r,c+1)
#         if r<n-1 and maze[r+1][c]==0:
#             for item in findPath(r+1,c):
#                 yield [(r,c)]+item #findPath(r+1,c)
#         if c>0 and maze[r][c-1]==0:
#             for item in findPath(r,c-1):
#                 yield [(r,c)]+item #findPath(r,c-1)
#         if r>0 and maze[r-1][c]==0:
#             for item in findPath(r-1,c):
#                 yield [(r,c)]+item #findPath(r-1,c)

#         maze[r][c] = 0

n=6
# def findPath(i,j):
#     if i==n-1 and j==n-1:
#         return [(i,j)]
#     if maze[i][j]==0:
#         maze[i][j]=2
#         if j<n-1 and maze[i][j+1]==0:
#             for item in findPath(i,j+1):
#                 yield [(i,j)] + item 
#         if i<n-1 and maze[i+1][j]==0:
#             for item in findPath(i+1,j):
#                 yield [(i,j)] + item 
#         if j>0 and maze[i][j-1]==0:
#             for item in findPath(i,j-1):
#                 yield [(i,j)] + item 
#         if i>0 and maze[i-1][j]==0:
#             for item in findPath(i-1,j):
#                 yield [(i,j)] + item 
#         maze[i][j]=0

def findPath(i,j,path=[]):
    if i==n-1 and j==n-1:
        return path+[(i,j)]
    if maze[i][j]==0:
        path.append((i,j))
        maze[i][j]=2
        if j<n-1 and maze[i][j+1]==0:
            yield findPath(i,j+1,path+[(i,j)])
            # for item in findPath(i,j+1,path):
            #     yield [(i,j)]+item
        if i<n-1 and maze[i+1][j]==0:
            yield findPath(i+1,j,path+[(i,j)])
            # for item in findPath(i+1,j,path):
            #     yield [(i,j)]+item
        if j>0 and maze[i][j-1]==0:
            yield findPath(i,j-1,path+[(i,j)])
            # for item in findPath(i,j-1,path):
            #     yield [(i,j)]+item 
        if i>0 and maze[i-1][j]==0:
            yield findPath(i-1,j,path+[(i,j)])
            # for item in findPath(i-1,j,path):
            #     yield [(i,j)]+item 
        maze[i][j]=0

# print(list(findPath(0,0)))
# print(findPath(0,0))
for x in findPath(0,0):
    print(x)
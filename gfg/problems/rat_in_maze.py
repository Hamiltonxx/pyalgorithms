# def findPath(maze,n,i,j,path):
#     if i<0 or j<0 or i>=n or j>=n or maze[i][j]!=1:
#         return
#     path.append((i,j))
#     if i==n-1 and j==n-1:
#         p=""
#         for x,y in zip(path,path[1:]):
#             if y[0]==x[0]+1:
#                 p += "D"
#             elif y[0]==x[0]-1:
#                 p += "U"
#             elif y[1]==x[1]+1:
#                 p += "R"
#             else:
#                 p += "L"
#         global res
#         res.append(p)
#     else:
#         maze[i][j] = 2
#         findPath(maze,n,i,j+1,path)
#         findPath(maze,n,i+1,j,path)
#         findPath(maze,n,i,j-1,path)
#         findPath(maze,n,i-1,j,path)
#         maze[i][j] = 1

#     path.pop()

def findPath(maze,n):
    res = []
    
    def findPathUtil(maze,n,i,j,path):
        if i<0 or j<0 or i>=n or j>=n or maze[i][j]!=1:
            return
        path.append((i,j))
        if i==n-1 and j==n-1:
            p=""
            for x,y in zip(path,path[1:]):
                if y[0]==x[0]+1:
                    p += "D"
                elif y[0]==x[0]-1:
                    p += "U"
                elif y[1]==x[1]+1:
                    p += "R"
                else:
                    p += "L"
            res.append(p)
        else:
            maze[i][j] = 2
            findPathUtil(maze,n,i,j+1,path)
            findPathUtil(maze,n,i+1,j,path)
            findPathUtil(maze,n,i,j-1,path)
            findPathUtil(maze,n,i-1,j,path)
            maze[i][j] = 1
        path.pop()

    findPathUtil(maze,n,0,0,[])
    res.sort()
    return " ".join(res)



T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    maze = [arr[i*n:(i+1)*n] for i in range(n)]
    # print(maze)
    # res = []
    # findPath(maze,n,0,0,[])
    print(findPath(maze,n))



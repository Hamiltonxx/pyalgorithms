# maze = [[0, 0, 1, 1, 1, 1],
#         [1, 0, 0, 0, 1, 1],
#         [0, 1, 0, 1, 0, 0],
#         [0, 0, 0, 1, 0, 1],
#         [1, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0]]
maze = [[0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

def findPath(r,c,path=[]):
    if r==5 and c==5:
        path.append((r,c))
        print(path)
        return path 
        # res = ""
        # for x,y in zip(path,path[1:]):
        #     if x[0]==y[0]:
        #         if y[1]>x[1]: res+="R"
        #         else: res+="L"
        #     else:
        #         if y[0]>x[0]: res+="D"
        #         else: res+="U"
        # exit(print(res))
    elif maze[r][c]==0:
        path.append((r,c))
        maze[r][c]=2
    
    if c<5 and maze[r][c+1]==0:
        path = findPath(r,c+1,path)
    if r<5 and maze[r+1][c]==0:
        path = findPath(r+1,c,path)
    if c>0 and maze[r][c-1]==0:
        path = findPath(r,c-1,path)
    if r>0 and maze[r-1][c]==0:
        path = findPath(r-1,c,path)

    path.pop()
    return path 

findPath(0,0,[])
# print(p)
# print("No path")
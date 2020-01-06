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

def findPath(r,c,path=[]):
    if r==5 and c==5:
        path.append((r,c))
        yield path
        # yield (5,5)
        return
    elif maze[r][c] == 0:
        # path.append((r,c))
        maze[r][c] = 2

    if c<5 and maze[r][c+1]==0:
        # yield [(r,c)] + list(findPath(r,c+1))
        yield [(r,c)]
        for x in findPath(r,c+1):
            yield x
    if r<5 and maze[r+1][c]==0:
        # yield [(r,c)] + list(findPath(r+1,c))
        yield (r,c)
        # yield findPath(r+1,c)
        for x in findPath(r+1,c):
            yield x
    if c>0 and maze[r][c-1]==0:
        # yield [(r,c)] + list(findPath(r,c-1))
        yield (r,c)
        # yield findPath(r,c-1)
        for x in findPath(r,c-1):
            yield x
    if r>0 and maze[r-1][c]==0:
        # yield [(r,c)] + list(findPath(r-1,c))
        yield (r,c)
        # yield findPath(r-1,c)
        for x in findPath(r-1,c):
            yield x

    # maze[r][c] = 0


print(list(findPath(0,0)))
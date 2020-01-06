maze = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0]]

def visit(r,c):
    if r==5 and c==5:
        print("Solved, Getting out!")
        return True 
    elif maze[r][c]==1:
        print("Wall at",r,c)
        return False 
    elif maze[r][c]==2:
        print("Have visited",r,c)
        return False 
    print("visiting...",r,c)
    maze[r][c] = 2

    # visit next clockwise, the right first
    if (c<5 and visit(r,c+1) or r<5 and visit(r+1,c) or 
        c>0 and visit(r,c-1) or r>0 and visit(r-1,c)):
        return True 
    return False 

visit(0,0)
# print(p)

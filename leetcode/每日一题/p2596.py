# legal = lambda x,y: {abs(x[0]-y[0]),abs(x[1]-y[1])} == {1,2}
from itertools import product
def checkValidGrid(grid):
    if grid[0][0]!=0: return False
    n = len(grid)
    pre = [0,0]
    legal = lambda x,y: abs(x[0]-y[0]) * abs(x[1]-y[1]) == 2
    for i in range(1,n*n):
        for r,c in product(range(n), range(n)):
            if grid[r][c] == i:
                if legal([r,c], pre):
                    pre = [r,c]
                else:
                    return False
                break
        else:
            return False
    return True

# grid = [[24,11,22,17,4],
#         [21,16,5,12,9],
#         [6,23,10,3,18],
#         [15,20,1,8,13],
#         [0,7,14,19,2]]
grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]

print(checkValidGrid(grid))
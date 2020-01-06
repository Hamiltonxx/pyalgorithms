
mtx = [[0,0,0],
     [0,1,0],
     [1,1,1]]

n = len(mtx[0])

def backtrack(i,j):
    if mtx[i][j] == 0:
        return 0
    # if j<n-1 and mtx[i][j+1]==0 or i<n-1 and mtx[i+1][j]==0 or j>0 and mtx[i][j-1]==0 or i>0 and mtx[i-1][j]==0:
    #     return 1
    mtx[i][j] = -1
    if j<n-1 and mtx[i][j+1]!=-1:
        return backtrack(i,j+1) + 1
    if i<n-1 and mtx[i+1][j]!=-1:
        return backtrack(i+1,j) + 1
    if j>0 and mtx[i][j-1]!=-1:
        return backtrack(i,j-1) + 1
    if i>0 and mtx[i-1][j]!=-1:
        return backtrack(i-1,j) + 1

    mtx[i][j] = 1

print(backtrack(2,2))

# res = [[-2]*n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         res[i][j] = backtrack(i,j)
# print(res)


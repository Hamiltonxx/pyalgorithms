mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]

def diagonal_sum(mat):
    sm = 0
    n = len(mat)
    for i in range(n):
        sm += mat[i][i] + mat[i][n-1-i]
    if n&1:
        sm -= mat[n//2][n//2]
    return sm

print(diagonal_sum(mat))
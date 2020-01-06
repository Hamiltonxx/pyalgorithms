# 1 0 1 1 1
# 1 1 1 0 1
# 0 0 0 0 1
# 0 0 0 0 1
# 0 0 0 0 1

def backtrack(i,j,mtx,n,s):
    if i==n-1 and j==n-1:
        global output 
        output = output + s + " "
        # s = ""
        return
    
    if j<n-1 and mtx[i][j+1]==1:
        # s += "R"
        a = s 
        mtx[i][j] = 2
        backtrack(i,j+1,mtx,n,s)
    if i<n-1 and mtx[i+1][j]==1:
        # s += "D"
        a = s + "D"
        mtx[i][j] = 2
        backtrack(i+1,j,mtx,n,a)
    if j>0 and mtx[i][j-1]==1:
        # s += "L"
        a = s + "L"
        mtx[i][j] = 2
        backtrack(i,j-1,mtx,n,a)
    if i>0 and mtx[i-1][j]==1:
        # s += "U"
        a = s + "U"
        mtx[i][j] = 2
        backtrack(i-1,j,mtx,n,a)

    mtx[i][j] = 1
    return

# def findPath(mtx,n):
#     global output 
#     output = ""
#     backtrack(0,0,mtx,n,"")
#     return output

T = int(input())
for _ in range(T):
    n = int(input())
    lst = list(map(int,input().split()))
    mtx = [lst[i*n:i*n+n] for i in range(n)]

    output = ""

    # print(findPath(mtx,n))
    backtrack(0,0,mtx,n,"")
    print(output)
    

output = ""

def backtrack(i,j,mtx,n,s):
    if i==n-1 and j==n-1:
        global output 
        output = output + s + " "
        return
    
    if j<n-1 and mtx[i][j+1]==1:
        s += "R"
        mtx[i][j] = 2
        backtrack(i,j+1,mtx,n,s)
    if i<n-1 and mtx[i+1][j]==1:
        s += "D"
        mtx[i][j] = 2
        backtrack(i+1,j,mtx,n,s)
    if j>0 and mtx[i][j-1]==1:
        s += "L"
        mtx[i][j] = 2
        backtrack(i,j-1,mtx,n,s)
    if i>0 and mtx[i-1][j]==1:
        s += "U"
        mtx[i][j] = 2
        backtrack(i-1,j,mtx,n,s)

    mtx[i][j] = 1
    return

def findPath(mtx,n):
    global output 
    output = ""
    backtrack(0,0,mtx,n,"")
    return output

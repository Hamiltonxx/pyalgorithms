def minTrioDegree(n, edges):
    mat = [[0]*n for _ in range(n)]
    deg = [0] * n 
    mn = float('inf')

    for i,j in edges:
        mat[i-1][j-1] = True
        mat[j-1][i-1] = True 
        deg[i-1] += 1
        deg[j-1] += 1

    for i in range(n):
        for j in range(i+1,n):
            if mat[i][j]:
                for k in range(j+1,n):
                    if mat[i][k] and mat[j][k]:
                        mn = min(mn, deg[i]+deg[j]+deg[k]-6)

    return -1 if mn==float('inf') else mn

    
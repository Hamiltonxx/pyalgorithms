# dp[i][j] 定义为以(i,j)位置为右下角的矩形区域内的苹果数量
# 状态转移方程为: 
# dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + (pizza[i][j]=='A)

# def ways(pizza, k):
#     rows, cols = len(pizza), len(pizza[0])
#     dp = [[0]*cols for _ in range(rows)]
#     for i in range(rows):
#         for j in range(cols):
#             dp[i][j] = (dp[i-1][j] if i>0 else 0) + (dp[i][j-1] if j>0 else 0) - (dp[i-1][j-1] if i>0 and j>0 else 0) + (pizza[i][j]=='A')
    
#     def dfs(r, c, cuts):
#         if dp[r][c] == 0:
#             return 0
#         if cuts == k-1:
#             return 1
#         result = 0
#         for i in range(r+1, rows):
#             if dp[i][c] > 0:
#                 result += dfs(i, c, cuts+1)
#         for j in range(c+1, cols):
#             if dp[r][j] > 0:
#                 result += dfs(r, j, cuts+1)
#         return result
    
#     return dfs(0,0,0)



# import functools

# def ways(pizza, k):
#     rows, cols = len(pizza), len(pizza[0])
#     @functools.lru_cache(None)
#     def f(x, y, k):
#         if not k:
#             return any('A' in p[y:cols] for p in pizza[x:rows])
#         res = 0
#         for i in range(x+1, rows):
#             if any('A' in p[y:cols] for p in pizza[x:i]):
#                 res += f(i, y, k-1)
#         for j in range(y+1, cols):
#             if any('A' in p[y:j] for p in pizza[x:rows]):
#                 res += f(x, j, k-1)
#         return res
#     return f(0, 0, k-1) % (10**9+7)

from functools import lru_cache
from itertools import product
def ways(pizza, k):
    m, n = len(pizza), len(pizza[0])

    @lru_cache(None)
    def dfs(k, i=0, j=0, res=0):
        if not (0<=i<m and 0<=j<n): return 0
        for x,y in product(range(i,m), range(j,n)):
            if pizza[x][y] == 'A':
                if not k: return 1
                res += sum(dfs(k-1,X,j) for X in range(x+1,m))
                break
        for y,x in product(range(j,n), range(i,m)):
            if pizza[x][y] == 'A':
                if not k: return 1
                res += sum(dfs(k-1,i,Y) for Y in range(y+1,n))
                break
        return res
    
    return dfs(k-1) % 1000000007

pizza = ["A..","AAA","..."]
k = 3
print(ways(pizza,k))
# dp[i][j]定义为i个0和j个1时的最大子集长度
# dp[i][j] = max(dp[i][j], dp[i-s.count('0)][j-s.count('1')]+1)
def findMaxForm(strs, m, n):
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for s in strs:
        c0 = s.count('0')
        c1 = len(s) - c0
        for i in range(m, c0-1, -1):
            for j in range(n, c1-1, -1):
                dp[i][j] = max(dp[i][j], dp[i-c0][j-c1]+1)
    
    return dp[m][n]

# strs = ["10", "0001", "111001", "1", "0"]
strs = ["10", "0", "1"]
print(findMaxForm(strs, 1, 1))
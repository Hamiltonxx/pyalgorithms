def numTrees(n):
    dp = [1] + [0] * n
    for i in range(1,n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]

def lps(s):
    # dp[i][j]定义为子串s[i...j]中最长回文子序列的长度
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    # 从左下角向右上角移动
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][-1]

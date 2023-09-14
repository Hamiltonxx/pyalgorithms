# def longestCommonSubsequence(text1, text2):
#     m,n = len(text1),len(text2)
#     dp = [[0]*(n+1) for _ in range(m+1)]

#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if text1[i-1] == text2[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1
#             else:
#                 dp[i][j] = max(dp[i][j-1], dp[i-1][j])

#     return dp[m][n]

def longestCommonSubsequence(s1, s2):
    m, n = len(s1), len(s2)
    bef, aft = [0]*(n+1), [0]*(n+1)
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                aft[j+1] = 1 + bef[j]
            elif aft[j] > bef[j+1]:
                aft[j+1] = aft[j]
            else:
                aft[j+1] = bef[j+1]
        aft, bef = bef, aft
    return bef[-1]
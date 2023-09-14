def wordBreak(s, wordDict):
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True
    for j in range(1,n+1):
        for word in wordDict:
            m = len(word)
            if j >= m:
                dp[j] = dp[j] or (dp[j-m] and s[j-m:j]==word)
    return dp[n]

# def wordBreak(s, wordDict):
#     n = len(s)
#     dp = [False] * (n+1)
#     dp[0] = True 
#     mx = max(map(len, wordDict))

#     for i in range(1, n+1):
#         for j in range(i-1, max(i-mx-1, -1), -1):
#             if dp[j] and s[j:i] in wordDict:
#                 dp[i] = True
#                 break

#     return dp[n]
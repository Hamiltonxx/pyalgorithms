# def minDistance(word1, word2):
#     m,n = len(word1), len(word2)
#     dp = [[0]*(n+1) for _ in range(m+1)]
#     for j in range(n+1):
#         dp[0][j] = j
#     for i in range(m+1):
#         dp[i][0] = i
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if word1[i-1] == word2[j-1]:
#                 dp[i][j] = dp[i-1][j-1]
#             else:
#                 dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
#     return dp[-1][-1]

word1 = "sea"
word2 = "eat"
# word1 = "leetcode"
# word2 = "etco"

from collections import defaultdict 
import bisect

def lcs(word1, word2):
    l1, l2 = len(word1), len(word2)
    d = defaultdict(list)
    for i,x in enumerate(word2):
        d[x].append(i)
    n = max(l1, l2)
    dp = [n+1] * (n+1)
    for x in word1:
        if x not in d:
            continue
        for i in reversed(d[x]):
            idx = bisect.bisect_left(dp, i)
            dp[idx] = i
    return bisect.bisect_left(dp, n+1)

def minDistance(word1, word2):
    l1, l2 = len(word1), len(word2)
    d = defaultdict(list)
    for i,x in enumerate(word2):
        d[x].append(i)
    n = max(l1, l2)
    dp = [n+1] * (n+1)
    for x in word1:
        if x not in d:
            continue 
        for i in reversed(d[x]):
            idx = bisect.bisect_left(dp, i)
            dp[idx] = i
    return l1 + l2 - 2 * bisect.bisect_left(dp, n+1)


print(minDistance(word1, word2))
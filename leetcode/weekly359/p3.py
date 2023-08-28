def max_profit(n, offers):
    dp = [0] * (n+1)
    ends = [[] for _ in range(n)] # 截至每个结束日的offer列表
    for s,e,g in offers:
        ends[e].append((s,g))

    for i in range(n):
        dp[i+1] = dp[i]
        for s,g in ends[i]:
            dp[i+1] = max(dp[i+1], dp[s]+g)

    return dp[-1]

# n = 5
# offers = [[0,0,1],[0,2,2],[1,3,2]]
# offers = [[0,0,1],[0,2,10],[1,3,2]]
n = 10
offers = [[0,6,5],[2,9,4],[0,9,2],[3,9,3],[1,6,10],[0,1,3],[3,8,9],[4,8,3],[2,6,5],[0,4,6]]
print(max_profit(n,offers))

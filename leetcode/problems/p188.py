def maxProfit(K, prices):
    dp = [[1000,0] for _ in range(K+1)]
    # dp[k][0]定义为<=k次交易前，你需要支付的最小费用
    # dp[k][1]定义为<=k次交易前，你能获取的最大收益
    for price in prices:
        for k in range(1, K+1):
            dp[k][0] = min(dp[k][0], price - dp[k-1][1])
            dp[k][1] = max(dp[k][1], price - dp[k][0])
    return dp[K][1]

def max_profit(k, prices):
    cost = [1000] * (k+1)
    profit = [0] * (k+1)
    for price in prices:
        for i in range(1, k+1):
            cost[i] = min(cost[i], price - profit[i-1])
            profit[i] = max(profit[i], price - cost[i])
    return profit[k]
    

# import random 
# prices = [random.randint(1,20) for _ in range(12)]
# print(prices)
prices = [1, 11, 19, 18, 13, 17, 10, 9, 19, 3, 14, 4]
# print(maxProfit(2, prices))
# print(max_profit(2, prices))
# print(maxProfit(3, prices))
print(max_profit(3, prices))